from django.contrib import admin

# Register your models here.

from base_app.models import Message, Room, Topic

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)