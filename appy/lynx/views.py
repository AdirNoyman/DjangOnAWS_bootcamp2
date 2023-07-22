from django.shortcuts import render

from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, UpdateUserForm, UpdateProfileForm
from . models import Profile
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    return render(request, 'lynx/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        # Get user form data and use it to create a new user
        form = CreateUserForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the user only to form memory before saving to the database, so we can modify the user before saving
            current_user = form.save(commit=False)
            # Save the user
            form.save()
            # Get the username
            username = form.cleaned_data.get('username')
            # Send a message to the user
            print('Account was created for ' + username)
            profile = Profile.objects.create(user=current_user)
            # Redirect the user to the login page
            return redirect("login")
    # Get form data and it to the register page data context
    context = {'form': form}

    return render(request, 'lynx/register.html', context=context)


@login_required(login_url='login')
def dashboard(request):
    profile_pic = Profile.objects.get(user=request.user)
    context = {'profile_avatar': profile_pic}
    return render(request, 'lynx/dashboard.html', context=context)


def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        # Get user form data and use it to create a POST request
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            # Get the username and password
            username = request.POST.get('username')
            password = request.POST.get('password')
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            # Check if the user is authenticated
            if user is not None:
                # Login the user
                auth.login(request, user)
                # Redirect the user to the dashboard
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'lynx/my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect('')


@login_required(login_url='login')
def profile_management(request):
    # Load current user signed into the user form
    user_form = UpdateUserForm(instance=request.user)
    # Get the profile picture of the user that is signed in
    profile = Profile.objects.get(user=request.user)
    # Load the profile picture of the current user to the profile form
    profile_form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, request.FILES, instance=profile)
        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')

        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'lynx/profile-management.html', context=context)


@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.delete()
        return redirect('')
    return render(request, 'lynx/delete-account.html')
