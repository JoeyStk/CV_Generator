from django.urls import path
from .views import WordExperienceView

urlpatterns = [
    path('', WordExperienceView.as_view(), name='experiences'),
]
