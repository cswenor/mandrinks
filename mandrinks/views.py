from django.shortcuts import render_to_response
from django.template import Context, loader
from django.http import HttpResponse
from mandrinks.models import Event

def index(request):
	events = Event.objects.all()
	t = loader.get_template('mandrinks/index.html')
	c = Context({
		'mdEvents': events,
	})
	return HttpResponse(t.render(c))