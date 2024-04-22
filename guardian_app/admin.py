from django.contrib import admin
from .views import send_notification
from fcm_django.models import FCMDevice
from fcm_django.admin import DeviceAdmin
from .models import *
from test_app.models import *
from guardian.admin import GuardedModelAdmin


admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(Employee)
admin.site.register(Soura)
admin.site.register(Image)
# admin.site.register(Test)

class MyAdmin(DeviceAdmin):
    actions = list(DeviceAdmin.actions) + ['send_notification']

    def send_notification(self, request, queryset):
        for obj in queryset:
            send_notification('My Title', 'My Body', obj.device_id)
    send_notification.short_description = "Send notification"


admin.site.unregister(FCMDevice)
admin.site.register(FCMDevice,MyAdmin)
