import imp
from .models import OrganizerPermission


def get_permissions(organizer):
    organizer_permission = OrganizerPermission.objects.get(user=organizer)
    all_permissions = organizer_permission.permission.exclude(url_name='qr-checkin').order_by('permission_name')
    permission_tuples = [(p.url_name,p.permission_name[2:]) for p in all_permissions]

    return permission_tuples
