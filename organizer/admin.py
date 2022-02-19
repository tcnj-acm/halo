from django.contrib import admin
from .models import OrganizerInfo, WebsiteSettings, FeaturePermission, OrganizerPermission
# Register your models here.
admin.site.register(OrganizerInfo)
admin.site.register(WebsiteSettings)
admin.site.register(FeaturePermission)
admin.site.register(OrganizerPermission)
