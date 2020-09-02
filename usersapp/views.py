from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect

# Create your views here.
from usersapp.models import Users


def login(request):
    context = {}
    if request.method == 'POST':
        useremail = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(useremail=useremail)
        except Users.DoesNotExist:
            context['error']='아이디 또는 비밀번호가 일치하지 않습니다.'
            return render(request,'login.html',context)
        else:
            user_name=user.username
            if check_password(password, user.password):
                request.session['user'] = user_name
                return redirect('mainapp/index/')
            else:
                context['error']='아이디 또는 비밀번호가 일치하지 않습니다.'
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        if request.POST.get['password'] ==request.POST.get['re_password']:
            useremail = request.POST.get('email', None)
            username = request.POST.get('name', None)
            password = request.POST.get('password', None)
            users = Users(
                useremail=useremail,
                username=username,
                password=make_password(password)
            )
            users.save()
            return render(request, 'login.html')
        else:
            context = {}
            context['error']='비밀번호가 일치하지 않습니다.'
            return render(request, 'register.html',context)
    else:
        return render(request,'register.html')