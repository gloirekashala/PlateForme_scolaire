from django.urls import path
from .views import DashboardComptable, formulaire

urlpatterns = [
    path('', DashboardComptable.as_view(), name="dashboard_comptable"),
    path('forms', formulaire, name="forms"),
]
