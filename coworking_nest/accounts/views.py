from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserChangeForm
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import logout



def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # Salvează utilizatorul nou
            login(request, user) # <--- Loghează userul imediat după înregistrare
            return redirect(reverse('spaces'))  # <--- Redirecționează la 'spaces'
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def account_overview(request):
    """
    Displays an overview of the authenticated user's account.
    """
    return render(request, 'accounts/account_overview.html', {'user': request.user})

@login_required
def profile_edit_view(request): # Numele funcției
    if request.method == 'POST':
        # Folosește un formular care preia datele userului curent
        form = UserChangeForm(request.POST, instance=request.user)
        # Sau UserProfileForm(request.POST, instance=request.user.userprofile) dacă ai un model UserProfile
        if form.is_valid():
            form.save()
            return redirect('profile') # Redirecționează înapoi la pagina de profil după salvare
    else:
        form = UserChangeForm(instance=request.user)
        # Sau UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile_edit.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('spaces')  # după login mergi spre pagina spațiilor
            else:
                form.add_error(None, "Nume utilizator sau parolă incorecte.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # după logout mergi înapoi la login


