
from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^logged_in/(?P<id>[0-9]+)$', views.logged_in),
    url(r'^login', views.login )

]
