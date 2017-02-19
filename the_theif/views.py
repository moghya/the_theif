from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from . import theTheif

def index(request):

    response = ""
    return HttpResponse(response)