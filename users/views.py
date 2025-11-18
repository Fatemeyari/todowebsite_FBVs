
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import User

def home(request):
    """ Render the home page. """
    return render(request, 'home.html')

def create_accounts(request):
    """ Create new accounts. """
    if request.method == 'POST':
        try:
            username=request.POST.get('username')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            if password1 != password2:
                return redirect('.' ,context={'message':'Passwords do not match'})
            else:
                password=password1
            if request.POST.get('email'):
                email=request.POST.get('email')
            else:
                email=None
            user=User.objects.create_user(username=username, password=password , email=email)
            user.save()
            return redirect('todo_list')
        except:
            return redirect('.' ,context={'message':'Something went wrong'})
    return render(request, 'account.html')




def change_password(request):
    """ Change password. """
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('.')
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('.')
        user=User.objects.get(username=username)
        user.password=password1
        user.set_password(password1)
        user.save()
        messages.success(request, "Password changed successfully. Please login again.")
        return redirect('login_view')
    return render(request, 'change_password.html')


def login_view(request):
    """ login view.  """
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
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
