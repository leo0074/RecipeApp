from django.shortcuts import render

from django.http import HttpResponse


def login(request):
    return HttpResponse("This iwll be the login page")