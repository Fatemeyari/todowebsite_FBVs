
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import User
from .forms import CreateAccountForm , ChangePasswordForm, LoginForm


def home(request):
    """ Render the home page. """
    return render(request, 'home.html')




def create_accounts(request):
    """ Create new accounts. """
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
        return redirect('.')
    else:
        form = CreateAccountForm()
    return render(request, 'account.html', {'form': form})




def change_password(request):
    """ Change password. """
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1 != password2:
                return messages.error(request, 'passwords don\'t match')
            else:
                user=User.objects.get(username=username)
                user.set_password(password1)
                user.save()
                return redirect('login_view')
        return redirect('.')
    else:
        form = CreateAccountForm()
    return render(request, 'change_password.html', {'form': form})


def login_view(request):
    """ login view.  """
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('todo_list')
        else:
            return render(request, 'login.html',
                          {"message":"Invalid username or password"})
    return render(request, 'login.html')



def logout_view(request):
    """ logout view. """
    request.session.flush()
    auth_logout(request)
    response = redirect('login_view')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response


