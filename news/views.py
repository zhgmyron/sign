from django.shortcuts import render,HttpResponseRedirect
from django.contrib import auth
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
            respone= HttpResponseRedirect('/event_manage/')
            return respone
        else:
            return render(request,'index.html',{'error':'username or password error!'})


def event_manage(request):
    username= request.session.get('user','')
    return render(request,"sign/event_manage.html",{"user":username})