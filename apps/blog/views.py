from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, YearArchiveView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from . import models, forms


class NotFoundView(TemplateView):
    template_name = "blog/404.html"

class InicioView(ListView):
    model: models.Articulo
    template_name = 'blog/inicio.html'
    context_object_name = 'articulos'
    paginate_by = 3
    queryset = models.Articulo.objects.filter(publicado=True)

class ArticuloDetailView(DetailView):
    model = models.Articulo
    template_name = 'blog/articulo.html'
    context_object_name = 'articulo'
    slug_field = 'slug'
    slug_url_kwarg = 'articulo_slug'

    def get_context_data(self, **kwargs):
        articulo_id = models.Articulo.objects.get(slug=self.kwargs['articulo_slug']).id
        context = super(ArticuloDetailView, self).get_context_data(**kwargs)
        context['form'] = forms.ComentarioForm
        context['comentarios'] = models.Comentario.objects.filter(articulo_id=articulo_id)
        context['es_comentarista'] = self.request.user
        return context
    
    def post(self, request, *args, **kwargs):
        form = forms.ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.articulo_id = models.Articulo.objects.get(slug=self.kwargs['articulo_slug']).id
            comentario.save()
            return redirect('apps.blog:articulo', articulo_slug=self.kwargs['articulo_slug'])
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ArticulosByCategoriaView(ListView):
    model = models.Categoria
    template_name = 'blog/categoria.html'
    context_object_name = 'articulos'
    paginate_by = 3

    def get_queryset(self):
        categoria_slug = self.kwargs['categoria_slug']
        categoria = get_object_or_404(models.Categoria, slug=categoria_slug)
        return models.Articulo.objects.filter(categoria=categoria, publicado=True)
    
    def get_context_data(self, **kwargs): 
        context = super(ArticulosByCategoriaView, 
                        self).get_context_data(**kwargs)
        context['categoria'] = models.Categoria.objects.get(
            slug=self.kwargs['categoria_slug'])
        return context 

class ArticulosByAutorView(ListView):
    model = User
    template_name = 'blog/autor.html'
    context_object_name = 'articulos'
    paginate_by = 3 

    def get_queryset(self):
        autor = self.kwargs['autor']
        autor = get_object_or_404(User, username=autor)
        return models.Articulo.objects.filter(autor=autor, publicado=True)

    def get_context_data(self, **kwargs): 
        context = super(ArticulosByAutorView, self).get_context_data(**kwargs)
        context['autor'] = User.objects.get(username=self.kwargs['autor'])
        return context 

class ArticulosByArchivoViews(YearArchiveView):
    model = models.Articulo
    template_name = 'blog/archivo.html'
    make_object_list = True
    context_object_name = 'articulos'
    paginate_by = 3
    date_field = 'creacion'
    allow_future = False

    def get_queryset(self):
        year = self.kwargs['year']
        month = self.kwargs['month']

        if year and month:
            return models.Articulo.objects.filter(creacion__year=year, creacion__month=month, publicado=True)
        else:
            return super().get_queryset()


class ArticuloCreateView(CreateView):
    model = models.Articulo
    template_name = 'blog/forms/crear_articulo.html'
    form_class = forms.ArticuloForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('apps.blog:inicio')


class ArticuloUpdateView(UpdateView):
    model = models.Articulo
    template_name = 'blog/forms/actualizar_articulo.html'
    form_class = forms.ArticuloForm
    slug_field = 'slug'
    slug_url_kwarg = 'articulo_slug'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Obtiene el artículo actualizado desde el contexto
        articulo = self.object
        # Genera la URL para la vista 'articulo' usando el slug actualizado del artículo
        return reverse('apps.blog:articulo', kwargs={'articulo_slug': articulo.slug})


class ArticuloDeleteView(DeleteView):
    model = models.Articulo
    template_name = 'blog/forms/eliminar_articulo.html'
    slug_field = 'slug'
    slug_url_kwarg = 'articulo_slug'
    success_url = reverse_lazy('apps.blog:inicio')


class ComentarioUpdateView(UpdateView):
    model = models.Comentario
    context_object_name = 'comentario'
    template_name = 'blog/forms/actualizar_comentario.html'
    form_class = forms.ComentarioForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('apps.blog:inicio')

class ComentarioDeleteView(DeleteView):
    model = models.Comentario
    context_object_name = 'comentario'
    template_name = 'blog/forms/eliminar_comentario.html'
    success_url = reverse_lazy('apps.blog:inicio')
