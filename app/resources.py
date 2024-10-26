# resources.py
from import_export import resources
from .models import Student

class LandingPageResource(resources.ModelResource):
    class Meta:
        model = Student
