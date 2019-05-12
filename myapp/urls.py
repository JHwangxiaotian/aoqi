from django.conf.urls import url

from . import views

urlpatterns = [
    url('select', views.hello),
    url('updata', views.updata)
]