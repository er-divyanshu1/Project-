from django.contrib import messages
from .models import Event
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
from .models import Event
from .forms import Edit_event

# Create your views here.
#@login_required(login_url='login')
def homePage(reuest):
    event = Event.objects.all()
    context = {'events':event}
   
    return render(reuest, "home.html",context)

def signupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        uemail=request.POST.get('email')
        upass=request.POST.get('pass')
        uconpas=request.POST.get('conpass')
        if upass != uconpas:
            messages.success(request,'Password is not same.')
        else:
            my_user=User.objects.create_user(uname,uemail,upass)
            my_user.save()
            #return HttpResponse("User has been Created.")
            return redirect('login')
            print(uname,uemail,upass,uconpas)
    return render(request,"sign.html")

def loginPage(request):
    if request.method=='POST':
        luser=request.POST.get('user')
        lpass=request.POST.get('pass')
        user=authenticate(request,username=luser,password=lpass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,'Username or password is incorrect !')
            #return HttpResponse("UserName or password is wrong")
            return redirect('login')
    return render(request,"login.html")

def logoutPage(request):
    logout(request)
    return redirect('/')

def create_event(request):
    if request.method=="POST":
        title = request.POST.get('title')
        dec = request.POST.get('content')
        img = request.FILES["image"]
        event =Event(title=title, img=img, dec=dec, user_id=request.user)
        event.save()
        messages.success(request,'Your event is Submited.')
        return redirect('create_event')
    return render(request, "create_event.html")

def like_post(request):
   
    return redirect ('home')

def event_detail(request,id):
    event=Event.objects.get(id=id)
    context ={'events':event}
    print(event)
    return render(request, "event_detail.html",context)

def delete(request,id):
    event=Event.objects.get(id=id)
    event.delete()
    messages.success(request,'Event has been deleted.')
    return redirect('/')

def edit(request,id):
    event=Event.objects.get(id=id)
    editevent = Edit_event(instance=event)
    if request.method=='POST':
        form= Edit_event(request.POST,instance=event)
        if form.is_valid():
            form.save()
            messages.success(request,'Post is successfully updated.')
            return redirect('/')

    return render(request ,'edit_event.html',{'edit_event':editevent})