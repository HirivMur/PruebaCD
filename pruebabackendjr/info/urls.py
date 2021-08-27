from django.conf.urls import url
from django.urls import path
from info.views import colonia, estado, municipio, colonia, colonia_cp,index


urlpatterns = [
    url(r'^home/$',index,name="index"),
	url(r'^info/api/v0/estado/$', estado.as_view(), name="estado"),
    url(r'^info/api/v0/municipio/$', municipio.as_view(), name="municipio"),
    url(r'^info/api/v0/colonia/$', colonia.as_view(), name="colonia"),
    path('info/api/v0/colonia/cp/<str:cp>/', colonia_cp.as_view(), name="colonia_cp"),
    
]