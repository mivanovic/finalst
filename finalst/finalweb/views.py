from django.shortcuts import render, render_to_response, RequestContext
from finalweb.models import Quote, Project, Reference

from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from finalweb.forms import EmailForm

from finalst import settings

# Create your views here.


def index(request):
    return render_to_response('index.html', {'quotes': Quote.objects.all(), 'latest_project':
        Project.objects.latest('id'), 'topthree': Project.objects.order_by('-complexity')[:3]})


def contact(request):
	return render(request, 'contact.html')


def aboutus(request):
	return render_to_response('index.html')


def news(request):
	return render_to_response('index.html')


def services(request):
	return render_to_response('services.html')


def gallery(request):
	return render_to_response('index.html')


def references(request):
	return render_to_response('reference.html', {'references': Reference.objects.order_by('-complexity')})


def static_page(request, page_alias):    # page_alias holds the part of the url
    try:
        return render_to_response('services.html', {'active': Service.objects.get(id=page_alias)})
    except Service.DoesNotExist:
        raise Http404("Page does not exist")

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def sendmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            try:
                fullemail = name + "<" + email + ">"

                send_mail(email, message, fullemail, [settings.EMAIL_HOST_USER])
                return HttpResponseRedirect('/contact/')
            except:
                return HttpResponseRedirect('/contact/')
        else:

            return HttpResponseRedirect('/contact/')
    else:
        return HttpResponseRedirect('/contact/')
