from django.shortcuts import render

def index(request):
    """home page for learning logs"""
    return render(request, 'learning_logs.xhtml')
