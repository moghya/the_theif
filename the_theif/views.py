from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
import json
from . import theTheif

def index(request):
    response = 'this is index page visit attendance page.'
    return HttpResponse(response)

def getattendance(request):
    username = request.GET.get('username',None)
    password = request.GET.get('password',None)
    if username and password:
        data = theTheif.getAttendance(username,password)
        response = json.dumps(data,indent=4)
        context = {
            'data':data
        }
        return render(request, 'attendance.html', context)
        #return HttpResponse(response)
    else:
        return HttpResponse('I need Username and Password.')

