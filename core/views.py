# Create your views here.
from django.shortcuts import render



def index(request):
	c = {}
	c['main'] = 'Hei verden'
	return render(request, "index.html", c)
