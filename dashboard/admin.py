from django.contrib import admin
from .models import AdminLog, Inquiry
# Register your models here.

admin.site.register(AdminLog)
admin.site.register(Inquiry)
