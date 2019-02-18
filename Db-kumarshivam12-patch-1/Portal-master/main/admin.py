from django.contrib import admin

# Register your models here.
from .models import Consumer_Db
from .models import Role_Per
admin.site.register(Consumer_Db)
admin.site.register(Role_Per)