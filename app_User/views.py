from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from app_User.models import User

# Create your views here.

class Login(TemplateView):
    template_name = "user/login.html"

class Register(TemplateView):
    model = User
    template_name = "user/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def post(self, request):
        nom = request.POST.get('nom')
        postnom = request.POST.get('postnom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')

        # Create a new user instance
        user = User(
            nom=nom,
            postnom=postnom,
            prenom=prenom,
            email=email,
            user_type= 4,  # Assuming 'eleve' is user type 7
            telephone=telephone,
        )

        # Generate a unique username
        user.generate_username()
        user.set_password(password) 
        user.save()

        # Redirect to the login page after successful registration
        return redirect('login')