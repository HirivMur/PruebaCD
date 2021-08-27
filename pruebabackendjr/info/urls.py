from django.conf.urls import url
from django.urls import path
from info.views import colonia, colonia_nombre, estado, estado_nombre, municipio, municipio_nombre, colonia, colonia_nombre, colonia_cp


urlpatterns = [
	url(r'^api/v0/estado/$', estado.as_view(), name="estado"),
    path('api/v0/estado/nombre/<str:nombre>/', estado_nombre.as_view(), name="estado_nombre"),
    url(r'^api/v0/municipio/$', municipio.as_view(), name="municipio"),
    path('api/v0/municipio/nombre/<str:nombre>/', municipio_nombre.as_view(), name="municipio_nombre"),
    url(r'^api/v0/colonia/$', colonia.as_view(), name="colonia"),
    path('api/v0/colonia/nombre/<str:nombre>/', colonia_nombre.as_view(), name="colonia_nombre"),
    path('api/v0/colonia/cp/<str:cp>/', colonia_cp.as_view(), name="colonia_cp"),
    
]