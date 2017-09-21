from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),  
    url(r'^display$', views.display),
    url(r'^delete/(?P<num>\d+)$', views.delete),
    url(r'^final/(?P<num>\d+)$', views.final),
]
