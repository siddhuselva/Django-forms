from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms1 import sinform, upform
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import decorators #for authentication
from django.views.generic import ListView
from django.views.generic.edit import CreateView,
from . models import *



def inform1(request):
    form = sinform(request.POST)

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data['uname1']
        upswd = form.cleaned_data['upswd1']
        user = authenticate(request,username=name,password=upswd)
        if user is not None:
            login(request,user)
        else:
            return HttpResponse("Enter a Valid Username & Password")
        return HttpResponse(name, upswd)
    return render(request, 'signin.html', {'form': sinform})


def upform1(request):
    form = upform(request.POST)

    if (request.method == 'POST' and form.is_valid()):

        name = form.cleaned_data['uname2']
        email = form.cleaned_data['uemail2']
        upswd = form.cleaned_data['upswd2']
        d = User.objects.all()
        u = []
        for k in d:
            u.append(k.username)
        if name in u:
            return HttpResponse('Already Exist')
        a = User.objects.create_user(name, email, upswd)
        a.save()
        return HttpResponse('signed Up')
    return render(request, 'signup.html', {'form': upform})


def jj(request):
    return JsonResponse({'name':'siddhu'})

class maya(ListView):
    model = User
    template_name = 'hhh.html'
    h = [1,2,3]

def may(request,ff):
    g = User.objects.get(ff)
    return render(request, 'rform.html', {'form': g.email})

class Newuser(CreateView):
    model = Allusers
    fields = ['uname','uemail','upswd']
    template_name = 'crview.html'



