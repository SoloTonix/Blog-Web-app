from django.shortcuts import render, redirect 
from .forms import RegisterUserForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def Register(request):

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid:
            form.save()
            messages.success(request, 'Congrats, Your account has been created')
            return redirect('Login')
        else:
            messages.warning(request, 'Sorry, something went wrong')
            return redirect('Login')
    else:
        form = RegisterUserForm()

    context = {'form':form}
    return render(request, 'users/register.html', context)
        
def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('home')
        else:
            messages.warning(request, 'Sorry, something went wrong')
            return redirect('Login') 

    return render(request, 'users/login.html')      

def Logout(request):
    logout(request)
    return redirect('Login')



