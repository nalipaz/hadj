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


class Dashboard(generic.DetailView):
    model = Dashboard
    template_name = 'hass/dashboard.html'


