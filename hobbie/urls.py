
from django.conf.urls import url
from hobbie import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^map$', views.mymap, name="mymap"),
    url(r'^map/savetrack$', views.savetrack, name="savetrack"),
    url(r'^map/gettrack$', views.gettrack, name="gettrack"),
]
