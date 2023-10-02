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
    date = models.CharField(max_length=255, null=True)
    description = models.TextField(max_length=255)
    show_in_cv = models.BooleanField()
    
    def __str__(self):
        return self.company_name + ' | ' + self.title


class PersonalInformation(models.Model):
    name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(blank=False)
    website_links = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to="images/", blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    zip_code = models.PositiveIntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.name} | {self.email}'