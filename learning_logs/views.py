from django.shortcuts import render, redirect 

from .models import Topic
from .forms import TopicForm

def index(request): 
    """The home page for Learning Log.""" 
    return render(request, 'learning_logs/index.xhtml')

def topics (request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.xhtml', context)

def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)

def new_topic(request):
    """adds new topic"""
    if request.method != 'POST':
        #no data submitted then create blank screen
        form = TopicForm()

    else: #POST data submitted then process
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    #displays a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)
            