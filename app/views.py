from tempfile import template
from django.shortcuts import render

def Home(request):
    template_name = 'index.html'
    return render(request,template_name)
# Create your views here.
