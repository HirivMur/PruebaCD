from django.conf.urls import url
from authentication.views import loginUser,logoutUser


urlpatterns = [
	url(r'^login/$', loginUser, name="login"),
	url(r'^logout/$', logoutUser, name="logout"),
    
]