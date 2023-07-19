from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.dates import YearArchiveView
from django.contrib.auth.models import User
from . import models


# Create your views here.
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