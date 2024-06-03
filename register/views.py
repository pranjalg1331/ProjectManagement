from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password 
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from . import models
import uuid
# Create your views here.
def signup(request):
   
    if request.method=='GET':
        form = CreateUserForm()
        
        context={
            'form':form
        }
        return render(request,'signup.html',context)
    else :
        form = CreateUserForm(request.POST)
       
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            # user.token=str(uuid.uuid4())
            # utils.send_email_token(user.email,user.token)
            user.save()
            login(request, user)
            request.session['user_email']=user.email
            return redirect('index')
        else:
            return render(request, 'signup.html', {'form': form})


    
def login_view(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user_data=request.POST
        error_msg=""
        password=user_data.get('password')
        email=user_data.get('email')
        user=models.Profile.objects.get(email=email)
        if user:
            flag = check_password(password, user.password)
            if flag:
                login(request,user)
                
                return redirect('projects')
            else:
                error_msg="wrong email or password"
                
        else:
            error_msg="email does not exist"
            
        
        
        return render(request, 'login.html', {'error': error_msg})

def logout_view(request):
    print("done")
    logout(request)
    return redirect('login')