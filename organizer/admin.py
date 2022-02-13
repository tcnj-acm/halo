from django.contrib import admin
from .models import OrganizerInfo, WebsiteSettings

# Register your models here.
admin.site.register(OrganizerInfo)
admin.site.register(WebsiteSettings)
