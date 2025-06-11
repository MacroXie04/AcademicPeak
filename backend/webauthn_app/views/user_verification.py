from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as django_logout
from webauthn_app.forms.UserLoginForm import UserLoginForm
from webauthn_app.forms.UserRegisterForm import UserRegisterForm
from webauthn_app.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Create UserProfile for the user
            profile = UserProfile(
                user=user,
                gender=form.cleaned_data.get('gender'),
                profile_img=form.cleaned_data.get('profile_img')
            )
            profile.save()

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, '/', {'form': form})


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()

    return render(request, '/', {'form': form})


@login_required
def logout(request):
    django_logout(request)
    return redirect('index')
