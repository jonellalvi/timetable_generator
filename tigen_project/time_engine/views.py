# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from time_engine.models import Plan


# Each view is it's own function.
# Each view takes at least one arg: HttpRequest object
# EAch view must return a HttpResponse object
# the HttpResponse object takes a string parameter which is the content of the page we're sending to the client requesting the view


def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    plan_list = Plan.objects.all()
    context_dict = {'allplans': plan_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('time_engine/index.html', context_dict, context)
    #return HttpResponse("Hello World! You're at the Time Engine Index! Woot!")

def options(request):
    return HttpResponse("This is the Preferences page.")

def engine(request):
    return HttpResponse("This is the Engine!")

def results(request):
    return HttpResponse("This is the results page.")