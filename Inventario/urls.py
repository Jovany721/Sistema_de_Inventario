from .views import HOME, eliminar_reg, search_bd
from .views import Consulta
from django.urls import path

urlpatterns = [
    path('', HOME , name='HOME'),
    path('consulta/', Consulta, name='Consulta'),
    path('consulta/eliminar_reg/<producto>', eliminar_reg),
    path('search_bd/<producto>', search_bd)
  

]
