from django.contrib import admin

from .models import Dashboard, HassEntity, Tab, SubTab

admin.site.register(Dashboard)
admin.site.register(Tab)
admin.site.register(SubTab)
admin.site.register(HassEntity)
