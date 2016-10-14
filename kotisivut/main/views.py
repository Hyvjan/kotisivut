from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth import authenticate, login
from main.models import viewCounter
from django.db.models import F

# Create your views here.
def index(request):
	viewCounter.objects.filter(counterName='index').update(views=F('views')+1)
	katselukerrat=viewCounter.objects.get(counterName='index')
	return render_to_response('main/index.html', {'katselukerrat': katselukerrat})

def cv(request):
	viewCounter.objects.filter(counterName='cv').update(views=F('views')+1)
	katselukerrat=viewCounter.objects.get(counterName='cv')
	return render_to_response('main/cv.html', {'katselukerrat': katselukerrat})
