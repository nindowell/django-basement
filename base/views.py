from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'var': 'hello world'}
    return render(request, 'base/index.html', context)
