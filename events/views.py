from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import Eventform
from .models import Event, Eventitems
from Trace.models import CustomUser, Whole
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/login/')
def events_view(request):
    user = request.user
    events = Event.objects.all().filter(user=user)
    event_names = [(event.name, event.id) for event in events]
    context = {
        'events': event_names,
    }
    return render(request, 'events/events.html', context)


def editevent_view(request, id):
    event = Event.objects.get(id=id)
    print(f"The event name is: {event.name}")
    if request.method == "POST":
        name = request.POST.get('eventName')
        print(f"The changed name is: {name}")
        event.name = name
        event.save()
        return redirect('events')
    
#AT FIRST I USED THIS THEN LATER ABOVE CODE WAS USED.
# def editevent_view(request, id):
#     event = get_object_or_404(Event, id=id, user=request.user)
#     if request.method == "POST":
#         form = Eventform(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('events')
#     else:
#         form = Eventform(instance=event)
    
#     return render(request, 'events/editevents.html', {'form':form})


@login_required(login_url='/login/')
def addevent_view(request):
    if request.method == "POST":
        form = Eventform(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            wintegrate = request.POST.get('wintegration')
            if wintegrate == "on":
                event.wintegrate = True
            else:
                event.wintegrate = False
            print(f"The wintegrate is: {event.wintegrate}")
            event.save()
            return redirect('events')
    else:
        form = Eventform()

    return render(request, 'events/addevent.html', {'form':form})


@login_required(login_url='/login/')
def eventitems_view(request, id):
    event = Event.objects.get(id=id)
    user = request.user
    items = Eventitems.objects.filter(user=user, event=event).order_by('-date')
    context = {
        'eid':id,
        'items':items,
    }
    return render(request, 'events/eventitems.html', context)



@login_required(login_url='/login/')
def eitemsadd_view(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        today = request.POST.get('today')
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        elif today:
            date = datetime.date.today()
        else:
            date = None
        user = request.user
        event = Event.objects.get(id=id)
        item = Eventitems(user=user, name=name, amount=amount, date=date, event=event)
        item.save()
        if event.wintegrate == True:
            Whole.objects.create(user=user, text=name, number=amount, date=date, event_id=item.id)

        return redirect('eventitems', id=id)
    return render(request, 'events/eitemadd.html', {'id':id})


def eitemremove_view(request, id, eid):
    item = Eventitems.objects.get(id=id)
    event = Event.objects.get(id=eid)
    if event.wintegrate == True:
        witem = Whole.objects.get(event_id=id)
        witem.delete()
    item.delete()
    return redirect('eventitems', id=eid)
    