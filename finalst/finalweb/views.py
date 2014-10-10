from django.shortcuts import render, render_to_response, RequestContext
from finalweb.models import Quote, Project, Service

# Create your views here.

def index(request):
	return render_to_response('index.html', {'quotes': Quote.objects.all(), 'latest_project': Project.objects.latest('id'),
								'topthree': Project.objects.order_by('-complexity')[:3]})

def contact(request):
	return render_to_response('contact.html')

def aboutus(request):
	return render_to_response('index.html')

def news(request):
	return render_to_response('index.html')

def services(request):
	return render_to_response('services.html', {'services': Service.objects.all()})

def gallery(request):
	return render_to_response('index.html')

def references(request):
	return render_to_response('index.html')

def static_page(request, page_alias):    # page_alias holds the part of the url
    try:
        return render_to_response('services.html', {'active': Service.objects.get(id=page_alias)})
    except Service.DoesNotExist:
        raise Http404("Page does not exist")
