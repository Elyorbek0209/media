from django.contrib import admin
from .models import Destination

# Register your models here.

class destinationAdmin(admin.ModelAdmin):

    list_display = ['name', 'img', 'desc', 'price', 'offer']


admin.site.register(Destination, destinationAdmin)


