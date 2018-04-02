# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


def roomSearch(request):
    return render(request, 'mainsite/roomSearch.html', {})
    pass


def courseSearch(request):
    return render(request, 'mainsite/courseSearch.html', {})
    pass


def emptyRoomSearch(request):
    return render(request, 'mainsite/emptyRoomSearch.html', {})
    pass


def roomBorrow(request):
    return render(request, 'mainsite/roomBorrow.html', {})
    pass


def teacherSearch(request):
    return render(request, 'mainsite/teacherSearch.html', {})
    pass
