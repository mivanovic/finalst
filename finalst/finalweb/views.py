from django.shortcuts import render, render_to_response, RequestContext
from finalweb.models import Quote, Reference
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from finalweb.forms import EmailForm
from finalst import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def index(request):
    return render_to_response('index.html', {
        'quotes': Quote.objects.all(),
        'top_three': Reference.objects.order_by('-complexity')[:3]})


def contact(request):
    return render(request, 'contact.html')


def references(request):
    return render_to_response('reference.html', {'references': Reference.objects.order_by('-complexity')})


def single_reference(request, reference):
    try:
        return render_to_response('single_reference.html', {'data': Reference.objects.get(id=reference)})
    except Reference.DoesNotExist:
        raise Http404('Page does not exists')


def send_email(request):
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
