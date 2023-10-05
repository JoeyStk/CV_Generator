"""
This module holds all models
"""
from django.contrib.auth.models import User
from django.db import models


class WorkingExperience(models.Model):
    """
    Model for working experience
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    from_date = models.DateField(max_length=255, null=True)
    until_date = models.DateField(max_length=255, null=True)
    description = models.TextField(max_length=255)
    show_in_cv = models.BooleanField()
    
    def __str__(self):
        return self.company_name + ' | ' + self.title


class PersonalInformation(models.Model):
    name = models.CharField(max_length=25, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(max_length=255, blank=False)
    website_links = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to="images/", blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    zip_code = models.PositiveIntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.name} | {self.email}'
    
class AcademicExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255, blank=False)
    course = models.CharField(max_length=255, blank=False)
    degree = models.CharField(max_length=255, blank=False)
    summary = models.TextField(blank=False)
    location = models.CharField(max_length=255, blank=False)
    date_achieved = models.DateField(blank=False)

    def __str__(self):
        return f'{self.degree}, {self.course} - {self.location}'
