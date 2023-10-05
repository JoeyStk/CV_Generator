from django.contrib import admin
from .models import WorkingExperience, PersonalInformation, AcademicExperience

# Register your models here.
admin.site.register(WorkingExperience)
admin.site.register(PersonalInformation)
admin.site.register(AcademicExperience)
