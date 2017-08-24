
from django.conf.urls import url
from hobbie import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
