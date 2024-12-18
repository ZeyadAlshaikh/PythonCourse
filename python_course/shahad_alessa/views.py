from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "shahad_alessa_index.html")
