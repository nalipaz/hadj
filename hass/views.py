from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Tab, SubTab, HassEntity


class Index(generic.ListView):
    context_object_name = 'Tabs'
    template_name = 'hass/index.html'

    def get_queryset(self):
        return Tab.objects.all()


