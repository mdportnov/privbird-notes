from django.apps import AppConfig


class SecnoteConfig(AppConfig):
    name = 'secnote'
    
    def ready(self):
        from . import signals