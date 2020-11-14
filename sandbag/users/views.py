from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import LoginForm,RegForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.conf import settings

#----------------function-------------
def save_user(username):
    # Type : String -> None
    """Save user 
    Save user to redis, then check the username whether is admin, if user is admin will not
    to save in redis, and it will check the user is already save or not. 
    User who in redis will save two data in redis. 
        One is list : xxx_user['','','false'], 
        and the other is zadd : score[xxx:0]. 
    Args :
        username : Check username 
    
    """
    if(username!='admin'):
        is_exist = False
        for key in settings.CACHE.scan_iter():
            is_exist=True if username in key else False
        if(is_exist==False):
            settings.CACHE.rpush(username+'_user','','','false')
            settings.CACHE.zadd("score",{username:0})
            print("add to redis")

# -----------------------------
def login(request):
    # Type : request -> render to index or login
    """Login 
    Check the user is login or not, if user already login, it will redirect to index.html, or 
    the user not login, will redirct to login.html.
    User want to login, it will check login_form, if the form is valid which means all field
    (Username, Password) correct will redirect to index, except user is admin. Or if the form
    isn't valid, it will show the error message in context, and the context will present in 
    html.
    """ 
    if request.user.is_authenticated:
        if(request.user.is_superuser):
            return HttpResponseRedirect('chart/')
        return HttpResponseRedirect('index/')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request,user)
            username = request.user.username
            save_user(username)
            if(username == 'admin'):
                return HttpResponseRedirect('chart/')
            return  HttpResponseRedirect('index/')
    else:
        login_form = LoginForm()
    context={}
    context['login_form']=  login_form
    return render(request,'user/login.html',context)

def register(request):
    # Type : request -> render to index or register
    """
    Check the user is login or not, if user already login, it will redirect to index.html, 
    or the user not login, will redirct to register.html.
    User want to register, it will check reg_form, if the form is valid which means all 
    field (Username, Password, Password_again, Token) correct will redirect to index. 
    Or if the form isn't valid, it will show the error message in context, and the 
    context will present in html.
    """ 
    if request.user.is_authenticated:
        return HttpResponseRedirect('index/')
    if request.method == 'POST':
        reg_form= RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data["username"]
            #email = reg_form.cleaned_data["email"]
            password=reg_form.cleaned_data["password"]
            reg_form.save()
            return HttpResponseRedirect('/')
    else:
        reg_form = RegForm()
    context={}
    context['reg_form'] = reg_form
    return render(request,'user/register.html',context)

def logout(request):
    auth.logout(request)  
    return redirect('/',name='logout')
 