from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('signup/', Register.as_view(), name="signup"),
]
