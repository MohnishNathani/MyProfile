from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html',{'insert_me':'LOL! My name is mohnish'})