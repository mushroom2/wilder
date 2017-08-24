from django.shortcuts import render
from django.views.generic import TemplateView
from hobbie.models import Card


def home(request):
    tasks = Card.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'hobbie/index.html', context)
