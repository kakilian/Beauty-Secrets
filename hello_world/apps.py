from django.apps import AppConfig


class HelloWorldConfig(AppConfig):
    default_auto_field = (
        "django.db.models.BigAutoField"  # Default primary key field type
    )
    name = "hello_world"  # The app name, matching the folder name
