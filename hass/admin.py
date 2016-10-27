from django.contrib import admin

from .models import HassEntity, Tab, SubTab

admin.site.register(HassEntity)
admin.site.register(Tab)
admin.site.register(SubTab)
