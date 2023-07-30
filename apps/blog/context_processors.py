from . import models 


def contexto_base(request):

    contexto = dict ()

     #Acerca de 
    if models.Acerca.objects.count():
          contexto['acerca'] = models.Acerca.objects.latest('creacion')
    else:
        contexto['acerca'] = ''

    # Categorías
    contexto['categorias'] = models.Categoria.objects.filter(activo=True)

    #Archivos
    contexto['archivos'] = [{'fecha':fecha} for fecha in models.Articulo.objects.dates('creacion', 'day', order='DESC').filter(publicado=True)]

    #Redes
    contexto['redes'] = models.Red.objects.all()

    return contexto