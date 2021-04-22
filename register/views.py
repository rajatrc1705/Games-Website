from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
def register(request):

    print(f"RESPONSE METHOD: {request.method}")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(f"Form Valid: {form.is_valid()}")
        if form.is_valid():
            user = form.save()
            return redirect('/')
    form = RegisterForm()
    return render(request, 'register/register.html', {'form': form})