from django.urls import path
from .views import WorkingExperienceView

urlpatterns = [
    path('', WorkingExperienceView.as_view(), name='experiences'),
]
