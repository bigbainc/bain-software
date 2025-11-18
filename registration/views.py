from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import StyledUserCreationForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('second_page')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            auth_login(request, form.get_user())
            messages.success(request, 'Welcome back!')
            return redirect('second_page')
        messages.error(request, 'Please double-check your username and password.')

    return render(request, 'registration/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('second_page')

    form = StyledUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('second_page')
        messages.error(request, 'Please fix the errors below and try again.')

    return render(request, 'registration/register.html', {'form': form})


@login_required
def second_page(request):
    return render(request, 'secondpage.html')

