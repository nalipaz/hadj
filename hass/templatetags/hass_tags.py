from django import template
from django.shortcuts import get_object_or_404, render
from hass.models import Tab, SubTab, HassEntity

register = template.Library()

# @register.inclusion_tag('hass/header.html', takes_context=True)
# def render_header(context, dashboard):
#     return {
#         'dashboard': dashboard
#     }
#
#
# @register.inclusion_tag('hass/footer.html', takes_context=True)
# def render_footer(context, dashboard):
#     return {
#         'dashboard': dashboard
#     }


@register.inclusion_tag('hass/tabs.html', takes_context=True)
def render_tabs(context, dashboard):
    tabs = Tab.objects.filter(dashboard=dashboard.id)
    return {
        'tabs': tabs,
        'dashboard': dashboard
    }


@register.inclusion_tag('hass/subtabs.html', takes_context=True)
def render_subtabs(context, tab):
    sub_tabs = SubTab.objects.filter(tab=tab.id)
    return {
        'sub_tabs': sub_tabs,
        'tab': tab
    }


@register.inclusion_tag('hass/entities.html', takes_context=True)
def render_entities(context, sub_tab):
    entities = HassEntity.objects.filter(sub_tab=sub_tab.id)
    return {
        'entities': entities,
        'sub_tab': sub_tab
    }


