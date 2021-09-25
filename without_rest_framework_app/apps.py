from django.apps import AppConfig


class WithoutRestFrameworkAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'without_rest_framework_app'
