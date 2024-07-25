from django.urls import path
from api_grupo_ka.view.orden_trabajo.views import ListOT,StateView
from api_grupo_ka.view.login.views import LoginView
urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("list/ot/",ListOT.as_view(),name="list_ot"),
    path("state/ot/",StateView.as_view(),name="state_ot")
]