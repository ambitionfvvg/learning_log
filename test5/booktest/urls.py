from django.conf.urls import url
from .import views


urlpatterns = [
        url(r'^$', views.index),
        # url(r'^(\d+)$', views.detail)
        url(r'^(?P<id>[0-9]+)$', views.detail)

]