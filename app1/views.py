from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("这是首页")
def bug():
    return HttpResponse("这是bug")