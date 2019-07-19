from django.shortcuts import render, HttpResponse, redirect
import bcrypt
from .models import Users
from django.contrib import messages
def index(request):
    return render(request, 'login_app/index.html')

def registration(request):

        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        else :
            last_name = request.POST['last_name']
            first_name = request.POST['first_name']

            email = request.POST['email']
            if request.POST['password1']==request.POST['password2']:
                password = bcrypt.hashpw(request.POST['password1'].encode(), bcrypt.gensalt())
            user = Users.objects.create(first_name=first_name, last_name=last_name, email=email,  password= password  )
            print(user.first_name)
            return redirect(f"/logged_in/{user.id}")

def logged_in(request, id):
    contain={
        'user' : Users.objects.get(id=id)
    }
    return render(request, 'login_app/login.html', contain)


def login (request):
    login_email = request.POST['login_email']
    user = Users.objects.get(email=login_email)
    hash1 = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    print(user.email, login_email)
    if bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode()):
        return redirect(f"/logged_in/{user.id}")
    else:
        return redirect('/')