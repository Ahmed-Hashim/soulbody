from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(EmployeeUser)
admin.site.register(ClientUser)