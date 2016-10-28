from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Dashboard, Tab, SubTab, HassEntity


class Dashboard(generic.DetailView):
    model = Dashboard
    template_name = 'hass/index.html'


