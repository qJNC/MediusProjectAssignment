from django.contrib import admin
from .models import uploader,files
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class VisualizerResource(resources.ModelResource):
    class Meta:
        model=files

class visualizerAdmin(ImportExportModelAdmin):
    resource_class = VisualizerResource
admin.site.register(uploader)
admin.site.register(files,visualizerAdmin)