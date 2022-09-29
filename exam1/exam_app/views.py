from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student(request):
    return HttpResponse('welcome django')

def hi(request):
    return render(request,'index.html')

def list(request):
    return render(request,'list.html')