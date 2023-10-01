from .models import WorkingExperience
from django.shortcuts import render
from django.views.generic import ListView

class WordExperienceView(ListView):
    template_name = "selection/work_experience_list.html"
    model = WorkingExperience

    def get_queryset(self):
        return WorkingExperience.objects.all()

    def get(self, request, *args, **kwargs):
        experiences = self.model.objects.all()
        context = {
            'experiences': experiences,
        }
        return render(
            request, self.template_name, context
        )
    
    def post(self, request, *args, **kwargs):
        selection = request.POST.getlist("show_in_cv")
        for experience in self.model.objects.all():
            if str(experience.id) in selection:
                WorkingExperience.objects.update_or_create(id=experience.id, user=request.user, defaults={"show_in_cv": True})
            else:
                WorkingExperience.objects.update_or_create(id=experience.id, user=request.user, defaults={"show_in_cv": False})
        experiences = self.model.objects.all()
        context = {
            'experiences': experiences,
        }
        return render(
            request, self.template_name, context
        )
