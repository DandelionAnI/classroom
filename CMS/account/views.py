# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import College, Student

# Create your views here.


def login(request):
    if request.method == 'POST':
        login = {}
        if request.POST:
            login['username'] = request.POST['username']
            login['password'] = request.POST['password']
            login['college'] = request.POST['usertype']

            user = Student.objects.filter(
                number__exact=login['username'],
                password__exact=login['password'],
                college__exact=login['college'],
            )
            if user:
                response = HttpResponseRedirect('/mainsite/')
                response.set_cookie('username', login['username'], 3600)
                return response
            else:
                return HttpResponse("not right!")
        pass
    else:
        college = College.objects.all()
        return render(request, 'account/login.html', {'college': college})


def index(request):
    hello = {"h1": "hello, world!"}
    return render(request, "account/index.html", {"hello": hello})


def register(request):
    return render(request, 'account/register.html', {})
    pass
