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
