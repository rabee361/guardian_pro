from django.contrib import admin
from .models import *
from guardian.admin import GuardedModelAdmin


class GuardAdmin(GuardedModelAdmin):
    pass

admin.site.register(Guard,GuardAdmin)



class testadmin(admin.ModelAdmin):
    readonly_fields=['serial']
admin.site.register(Test,testadmin)


