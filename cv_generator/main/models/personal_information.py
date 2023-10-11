from django.contrib.auth.models import User
from django.db import models

class PersonalInformation(models.Model):
    name = models.CharField(max_length=25, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, blank=False)
    website_links = models.URLField(blank=True)
    profile_photo = models.ImageField(upload_to="images/", blank=False)
    phone_number = models.PositiveIntegerField(blank=False)
    zip_code = models.PositiveIntegerField(blank=False)
    street = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return f'{self.name} | {self.email}'