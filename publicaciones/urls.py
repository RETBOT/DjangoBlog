# publicaciones/urls.py
from django.urls import path
from .views import (
    VistaListaPublicaciones,
    VistaCrearPublicacion,
    VistaEditarPublicacion,
    VistaDetallePublicacion,
    VistaEliminarPublicacion,
    )

urlpatterns = [
    path('',VistaListaPublicaciones.as_view(), name='lista_publicaciones'),
    # Publicaciones
    path('nueva/',VistaCrearPublicacion.as_view(), name='nueva_publicacion'),
    path('<int:pk>/detalle/',VistaDetallePublicacion.as_view(), name='detalle_publicacion'),
    path('<int:pk>/editar/',VistaEditarPublicacion.as_view(), name='editar_publicacion'),
    path('<int:pk>/eliminar/',VistaEliminarPublicacion.as_view(), name='eliminar_publicacion'),
]