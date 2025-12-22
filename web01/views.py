from django.shortcuts import render

def index(request):
    return render(request, 'web01/index.html')
