from django.apps import AppConfig

class FungiConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'fungi'

    def ready(self):
    	import fungi.signals