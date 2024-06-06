from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event

def event_list(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('event_list')  # Redirecionar de volta para a mesma página
    else:
        form = EventForm()
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events, 'form': form})
