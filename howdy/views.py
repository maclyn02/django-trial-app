from django.shortcuts import render
import os

# Create your views here.
def home_page(request):
    return render(request, 'index.html')
