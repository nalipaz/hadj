from django.conf.urls import url

from . import views

app_name = 'hass'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<dashboard_name>[0-9]+)/$', views.Index.as_view(), name='index'),
]

