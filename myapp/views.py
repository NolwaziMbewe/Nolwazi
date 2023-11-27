from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import LoginForm,Citizen
from .models import Users,Admin,Citizens
# Create your views here.

def home(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].title()
            password = form.cleaned_data['password'].title()
            if password == "2002":
                if Admin.objects.filter(username=username,password=password).exists():
                  return redirect(superuser)
                else:
                  message = "You dont have an account press sign up!"
                  return redirect(superuser)
            else:
                if Users.objects.filter(username=username,password=password).exists():
                    return redirect(userPanel) 
                else:  
                  return redirect(userPanel)
 
    else:
        form = LoginForm()
    return render(request,'home.html',{"form":form})

def sign(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].title()
            password = form.cleaned_data['password'].title()
            if Users.objects.filter(username=username,password=password).exists():
                  return redirect(home)
            else:
                 Users.objects.create(username=username,password=password)
                 return HttpResponse(users)
    else:
        form = LoginForm()
    return render(request,"signup.html",{"form":form})


def superuser(request):
    return render(request,'admin.html')


def users(request):
    user = Users.objects.all()
    return render(request,'userinfo.html',{'user':user})

def removeUser(request,id):
    user = get_object_or_404(Users,pk=id)
    user.delete()
    return redirect(users)


def updateUser(request,id):
    user = get_object_or_404(Users,pk=id)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
           user.username = form.cleaned_data['username'].title()
           user.password = form.cleaned_data['password'].title()
           user.save()
           return redirect(users)
        else:
            return HttpResponse('failed to updated user')
    else:
        form = LoginForm(initial={'username':user.username,'password':user.password})
    return render(request,'update.html',{'form':form,'user':user})


def userPanel(request):
    if request.method == 'POST':
        form = Citizen(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname= form.cleaned_data['lname']
            pob= form.cleaned_data['pob']
            fpob= form.cleaned_data['fpob']
            chief= form.cleaned_data['chief']
            postal= form.cleaned_data['postal']
            dob= form.cleaned_data['dob']
            gender= form.cleaned_data['gender']
            village= form.cleaned_data['village']
            province= form.cleaned_data['province']
            nrc= form.cleaned_data['nrc']
            cob= form.cleaned_data['cob']
            fdob= form.cleaned_data['fdob']
            district= form.cleaned_data['district']
            if Citizens.objects.filter(fname=fname,lname=lname,pob=pob,fpob=fpob,chief=chief,postal=postal,dob=dob,gender=gender,village=village,province=province,nrc=nrc,cob=cob,fdob=fdob,district=district).exists():
                return HttpResponse ('Account Already exists')
            else:
                Citizens.objects.create(fname=fname,lname=lname,pob=pob,fpob=fpob,chief=chief,postal=postal,dob=dob,gender=gender,village=village,province=province,nrc=nrc,cob=cob,fdob=fdob,district=district)
                return redirect(citz)
    else:
        form = Citizen()
    data = Citizens.objects.all()
    return render(request,'userPanel.html',{"form":form,"data":data})


def citz(request):
    data = Citizens.objects.all()
    return render(request,'citizens.html',{"data":data})