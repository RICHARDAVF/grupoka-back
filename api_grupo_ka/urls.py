from django.urls import path
from api_grupo_ka.view.orden_trabajo.views import ListOT,StateView
from api_grupo_ka.view.login.views import LoginView
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path("login/",LoginView.as_view(),name="login"),
    path("list/ot/",ListOT.as_view(),name="list_ot"),
    path("state/ot/",StateView.as_view(),name="state_ot")
    
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
