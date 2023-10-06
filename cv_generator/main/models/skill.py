from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,  MaxValueValidator
from django.db import models

SKILL_CHOICES = (
    ('LANGUAGE_SKILL', 'Language skills'),
    ('IT_SKILL', 'IT & Software skills'),
    ('OTHER_SKILL', 'Other skills'),
)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=SKILL_CHOICES)
    rating = models.IntegerField(default=5,
        validators=[
            MinValueValidator(0, message="Lowest possible skill level is 0"),
            MaxValueValidator(5, message="Highest possible skill level is 5")
        ]
    )

    def __str__(self):
        return self.skill