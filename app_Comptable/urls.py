from django.urls import path
from .views import DashboardComptable, formulaire

urlpatterns = [
    path('', DashboardComptable.as_view(), name="dashboard"),
    path('forms', formulaire, name="forms"),
]
