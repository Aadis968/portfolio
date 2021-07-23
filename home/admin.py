from django.contrib import admin
from .models import contactReport

class contactReportAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'subject', 'message', "date")
    
admin.site.register(contactReport, contactReportAdmin)

