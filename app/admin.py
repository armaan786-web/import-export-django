from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin
from .resources import LandingPageResource
# Register your models here.

class LandingPageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = LandingPageResource
    list_display = ("name",)


admin.site.register(Student, LandingPageAdmin)