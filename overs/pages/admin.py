from django.contrib import admin

from . import models

admin.site.register(models.Element)
admin.site.register(models.Plan)
admin.site.register(models.Wine)
admin.site.register(models.Advice)
admin.site.register(models.Risk)
admin.site.register(models.Task)
