from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Set the default auto-generated field to BigAutoField
    name = 'authentication' # Define the name of the authentication app