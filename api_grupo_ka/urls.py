from django.urls import path
from api_grupo_ka.view.orden_trabajo.views import ListOT 
urlpatterns = [
    path("list/ot/",ListOT.as_view(),name="list_ot")
]