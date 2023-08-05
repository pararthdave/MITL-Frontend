# djangotemplates/example/views.py
from django.shortcuts import render

# Add the two views we have been talking about  all this time :)
def index(request):
    return render(request, "index.html")
def register(request):
    return render(request, "register.html")
def selection(request):
    return render(request, "selection.html")
def dataset(request):
    return render(request, "dataset.html")

