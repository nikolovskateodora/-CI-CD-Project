from django.contrib import admin

# Register your models here.
from .models import Driver, Constructor

admin.site.register(Driver)
admin.site.register(Constructor)