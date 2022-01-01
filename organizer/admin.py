from django.contrib import admin
from .models import organizer, WaitingListControl, WaitingListSupervisors
# Register your models here.
admin.site.register(organizer)
admin.site.register(WaitingListControl)
admin.site.register(WaitingListSupervisors)
