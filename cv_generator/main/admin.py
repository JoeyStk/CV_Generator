from django.contrib import admin
from .models import Skill, PersonalInformation, WorkingExperience

# Register your models here.
admin.site.register(WorkingExperience)
admin.site.register(PersonalInformation)
admin.site.register(Skill)
