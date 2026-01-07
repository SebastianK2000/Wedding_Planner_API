from django.contrib import admin
from django.apps import apps

class NoLogAdmin(admin.ModelAdmin):
    def log_addition(self, request, object, message):
        pass

    def log_change(self, request, object, message):
        pass

    def log_deletion(self, request, object, object_repr):
        pass

app_config = apps.get_app_config('api')

for model in app_config.get_models():
    try:
        admin.site.register(model, NoLogAdmin)
    except admin.sites.AlreadyRegistered:
        pass