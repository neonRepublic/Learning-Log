from django.shortcuts import render 

from .models import Topic

def index(request): 
    """The home page for Learning Log.""" 
    return render(request, 'learning_logs/index.xhtml')

def topics (request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.xhtml', context)