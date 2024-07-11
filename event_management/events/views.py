# events/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Event
from .forms import EventForm

@csrf_exempt
def create_event_api(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return JsonResponse({'message': 'Event created successfully', 'event_id': event.id}, status=201)
        return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_event_list_api(request):
    events = Event.objects.all()
    data = [{'id': event.id, 'name': event.name, 'description': event.description,
             'date': event.date.strftime('%Y-%m-%d %H:%M:%S'), 'location': event.location,
             'organizer': event.organizer.username} for event in events]
    return JsonResponse(data, safe=False)

@csrf_exempt
def get_event_api(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'date': event.date.strftime('%Y-%m-%d %H:%M:%S'),
        'location': event.location,
        'organizer': event.organizer.username
    }
    return JsonResponse(data)

@csrf_exempt
def update_event_api(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'PUT':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Event updated successfully'}, status=200)
        return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_event_api(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'DELETE':
        event.delete()
        return JsonResponse({'message': 'Event deleted successfully'}, status=204)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
