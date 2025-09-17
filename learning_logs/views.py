from django.shortcuts import render, redirect, get_object_or_404 

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request): 
    """The home page for Learning Log.""" 
    return render(request, 'learning_logs/index.xhtml')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {"topics": topics}
    return render(request, 'learning_logs/topics.xhtml', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)
    
    # --- DEBUGGING LINE ---
    print(f"DEBUG: Retrieved topic with ID {topic.id} and name '{topic.text}'")
    # ----------------------
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)

def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)

def new_entry(request, topic_id):
    """Add a new entry for a topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.xhtml', context)