from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Dashboard, Tab, SubTab, HassEntity


def dashboard_view(request, dashboard_name):
    dashboard = get_object_or_404(Dashboard, name=dashboard_name)

    return render(request, 'hass/index.html', {'dashboard': dashboard})


