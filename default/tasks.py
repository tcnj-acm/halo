from __future__ import absolute_import, unicode_literals
from .models import CustomUser

def update_all_entities_age():
    users = CustomUser.objects.all()
    for user in users:
        user.save()
    return 'All entities updated successfully'