from django.contrib import admin
from sim_project.sim_app.models import Read

class ReadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'active_power',
        'reactive_power',
        'latest_status',
    )
admin.site.register(Read, ReadAdmin)