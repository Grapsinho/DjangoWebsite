from django.shortcuts import render,redirect
from .forms import UsersForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register(request):
    form = UsersForm()

    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'New account was created!')
            return redirect('login')

    context= {'form': form}
    return render(request, 'users/register.html', context)

def loginForm(request):

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context= {}
    return render(request, 'users/login.html', context)

def logoutForm(request):
    logout(request)
    return redirect('login')

def updateUser(request):
    user = request.user
    form = UpdateUserForm(instance=user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userProfile', pk=user.id)
    
    context = {'form': form}
    return render(request, 'playground/update_user.html', context)