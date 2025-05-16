from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from app_User.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'user/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Où sont mes données :", username, password)
        user = authenticate(request, username=username, password=password)
        print("C est quoi avec toi: ", user)

        if user is not None:
            login(request, user)
            print (login(request, user))
            return redirect('dashboard_comptable')
        else: 
            return render(request, 'user/login.html', {'error': "Veuillez saisir les bonnes informations"})

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