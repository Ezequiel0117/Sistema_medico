from django.apps import AppConfig

class SecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplication.security'  # Cambié 'app.security' por 'aplication.security'

    def ready(self):
        import aplication.security.signals  # Asegúrate de que la ruta sea la correcta
