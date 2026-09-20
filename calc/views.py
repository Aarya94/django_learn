from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home(request):
    return render(request, 'home.html', {'calc':'Suman'})
    return HttpResponse("Hello, welcome to the calculator app!!!")  
    return render(request, 'home.html',{'name':'Aaryan'})