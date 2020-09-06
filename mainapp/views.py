from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    if 'user' in request.session:
        context['user_name']=request.session.get('user')
        return render(request,'index.html',context)
    else:
        return render(request, 'index.html', context)

def logout(request):
    if 'user' in request.session:
        del request.session['email']
        del request.session['user']
        return render(request,'index.html',None)