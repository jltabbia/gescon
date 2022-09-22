from django.urls import path
from .views import EdificiosHomeView,AgregarView,eliminar,editar

app_name='edificios'

urlpatterns = [
    path('', EdificiosHomeView, name='home'),
    path('agregar/',AgregarView.as_view(),name="agregar"),
    path('eliminar/<int:id>', eliminar),
    path('editar/<int:id>',editar),

]