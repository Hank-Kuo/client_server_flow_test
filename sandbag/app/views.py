from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from users.models import User,Token




@user_passes_test(lambda u: u.is_staff,login_url='/')
@user_passes_test(lambda u: not u.is_superuser,login_url='/')
def index(request):
    context = {"index_page": "active"} 
    return render(request, 'index.html',context)

@user_passes_test(lambda u: u.is_staff,login_url='/')
def chart(request):
    context = {"chart_page": "active"}
    return render(request, 'chart.html',context)


@user_passes_test(lambda u: u.is_superuser,login_url='/')
def setting(request):
    context = {"setting_page": "active"}
    return render(request, 'setting.html',context)


@user_passes_test(lambda u: u.is_superuser,login_url='/')
def token(request):
    return render(request, 'setting-token.html')




