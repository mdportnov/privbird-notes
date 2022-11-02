from django.contrib import admin

from .models import *


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'main',
        'fake',
        'email',
    )


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    exclude = (
        'expiration_time',
        'password',
        'salt',
        'confirmation',
        'fake_note',
        'falsification',
    )
    
    search_fields = (
        'type',
        'auto_destruction',
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    exclude = (
        'content',
    )


@admin.register(Support)
class SupportAdmin(admin.ModelAdmin):
    list_display = (
        'problem',
        'email',
    )
    
    search_fields = (
        'email',
    )