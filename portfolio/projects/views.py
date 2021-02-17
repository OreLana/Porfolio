from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'projects/index.html', {})