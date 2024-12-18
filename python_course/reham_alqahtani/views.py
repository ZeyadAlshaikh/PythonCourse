from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "reham_alqahtani_index.html")
