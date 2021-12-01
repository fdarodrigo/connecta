# Django's imports
from django.contrib import admin

# Developer's import
from .models import Channel, Content


"""Registering models for system admin can edit the data"""


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    # Displaying data in admin panel
    list_display = ("name", "description")


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    # Displaying data in admin panel
    list_display = ("text", "image", "file")
