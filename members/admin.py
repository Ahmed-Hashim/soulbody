from django.contrib import admin
from .models import Profile, Chat, Messege, ChatNotification, AppDownLoad


class AppDownloadAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ('id', 'device_ip', 'country', 'date', 'deviceType')
    list_filter = ('date', 'country', 'deviceType')
    list_per_page = 25


admin.site.register(Profile)
admin.site.register(Chat)
admin.site.register(Messege)
admin.site.register(ChatNotification)
admin.site.register(AppDownLoad, AppDownloadAdmin)


# Register your models here.
