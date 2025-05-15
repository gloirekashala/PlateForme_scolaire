from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class DashboardComptable(TemplateView):
    template_name = "comptable/index.html"

def formulaire(request):
    return render(request, 'comptable/formulaire.html')