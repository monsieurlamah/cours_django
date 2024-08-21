from django.shortcuts import render, redirect
from account.forms.CustomUserLoginForm import CustomUserLoginForm
from account.forms.CustomUserRegisterForm import CustomUserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register_user(request):
    if request.method == "POST":
        form=CustomUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès !")
            return redirect('account-login')
        else:
            messages.error(request, "Merci de vérifier vos données")
    else:
        form = CustomUserRegisterForm()
    return render(request, 'account/register.html', {"form":form})

def login_user(request):
    if request.method == "POST":
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes connectés avec succès !')
                return redirect('dashboard_post')
            else:
                messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrect !")
        else:
            messages.error(request, "Merci de vérifier vos données !")
    else:
        form = CustomUserLoginForm()


    return render(request, 'account/login.html', {'form':form})

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Vous êtes deconnectés avec succès !')
    return redirect('account-login')