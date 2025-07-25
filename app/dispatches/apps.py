from django.apps import AppConfig


class DispatchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.dispatches'

    def ready(self):
        import app.dispatches.signals