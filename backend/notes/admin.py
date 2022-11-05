from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'expires', 'network')
    list_filter = ('expires', 'network')
    search_fields = ('slug',)
    exclude = ('real_content', 'fake_content', 'salt')
