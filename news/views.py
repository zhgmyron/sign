from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from news.models import Event
# Create your views here.
def index(request):
    return render(request,"sign/index.html")

def login_action(request):
    if request.method=='POST':
        username= request.POST.get('username','')
        password= request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user']=username
            respone= HttpResponseRedirect('/news/event_manage/')
            return respone
        else:
            return render(request,'sign/index.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
    event_list=Event.objects.all()
    username= request.session.get('user','')
    return render(request,"sign/event_manage.html",{"user":username,"events":event_list})

@login_required
def logout(request):
    auth.logout(request)
    response=HttpResponseRedirect('/index/')
    return response