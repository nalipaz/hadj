from django.db import models


class Dashboard(models.Model):
    name = models.CharField(max_length=128)
    theme = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Tab(models.Model):
    label = models.CharField(max_length=128)
    icon = models.CharField(max_length=128)

    def __str__(self):
        return self.label

class SubTab(models.Model):
    label = models.CharField(max_length=128)
    tab = models.ForeignKey(
        'Tab',
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return self.tab.label + " > " + self.label


class HassEntity(models.Model):
    entity_id = models.CharField(max_length=256)
    label = models.CharField(max_length=128)
    sub_tab = models.ForeignKey(
        'SubTab',
        on_delete=models.DO_NOTHING,
        null=True
    )

    def __str__(self):
        return self.sub_tab.tab.label + " > " + self.sub_tab.label + " > " + self.label + " (" + self.entity_id + ")"
