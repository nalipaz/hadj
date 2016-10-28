from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Dashboard, Tab, SubTab, HassEntity


class Index(generic.ListView):
    context_object_name = 'dashboards'
    template_name = 'hass/index.html'

    def get_queryset(self):
        return Dashboard.objects.all()


class DashboardDisplay(generic.DetailView):
    model = Dashboard
    template_name = 'hass/dashboard.html'


class SubTabList(generic.ListView):
    context_object_name = 'sub_tabs'
    template_name = 'hass/subtabs.html'

    def get_queryset(self):
        return SubTab.objects.filter(tab=self.kwargs['tab_id'])


