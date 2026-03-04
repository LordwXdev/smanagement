from django.contrib import admin
from .models import Message, Notification, Announcement
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Announcement)
