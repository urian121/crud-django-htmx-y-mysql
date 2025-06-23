from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='index'),
    path('modal-add-aspirante/', modal_add_aspirante, name='modal_add_aspirante'),
    path('agregar-aspirante/', add_aspirante, name='add_aspirante'),
    path('listar-aspirantes/', listar_aspirantes, name='listar_aspirantes'),
    path('cambiar-estado/<int:id_aspirante>/', cambiar_estado, name='cambiar_estado'),
    path('ver-aspirante/<int:id_aspirante>/', ver_aspirante, name='ver_aspirante'),
    path('modal-update-aspirante/<int:id_aspirante>/', modal_update_aspirante, name='modal_update_aspirante'),
    path('modal-delete-aspirante/<int:id_aspirante>/', modal_delete_aspirante, name='modal_delete_aspirante'),
    path('editar-aspirante/<int:id_aspirante>/', editar_aspirante, name='editar_aspirante'),
    path('eliminar-aspirante/<int:id_aspirante>/', eliminar_aspirante, name='eliminar_aspirante')
]