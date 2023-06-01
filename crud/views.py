from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def add_show(request):
    if request.method =="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # fm.save() #isse hum ek bar me sara data save kr sakte h 
           name= fm.cleaned_data['name']
           phone= fm.cleaned_data['phone']
           email= fm.cleaned_data['email']
           password= fm.cleaned_data['password']
           obj = User(name=name, phone=phone,email=email,password=password)
           obj.save() #object bana kar ek sath data save kr sakte h
           messages.add_message(request,messages.SUCCESS,"Your data has been submited successfully.")
           fm=StudentRegistration()
    else:
        fm = StudentRegistration()
    stud=User.objects.all()
    return render(request,'addandshow.html',{'form' :fm,'stud' :stud})


def delete_stud(request,id):
    if request.method=="POST":
        stu_id = User.objects.get(pk=id)
        stu_id.delete()
        messages.add_message(request, messages.SUCCESS,"Data has been deleted.")
        return HttpResponseRedirect('/')
    
    

def update_stud(request,id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
        fm.save()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request,"update.html",{'form' :fm})