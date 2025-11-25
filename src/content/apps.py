from django.apps import AppConfig

class ContentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content'

    def ready(self):
        # Implicitly import admin modules when app is ready to ensure registration
        # But wait, Django automatically looks for 'admin' module. 
        # Since 'admin' is now a package with __init__.py importing submodules, it should work fine.
        pass

