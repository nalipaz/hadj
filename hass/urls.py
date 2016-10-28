from django.conf.urls import url

from . import views

app_name = 'hass'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DashboardDisplay.as_view(), name='dashboard'),
    url(r'^tab/(?P<tab_id>[0-9]+)/$', views.SubTabList.as_view(), name='subtabs'),
]

