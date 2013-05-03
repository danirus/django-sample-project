from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext, loader


def http404(request):
    t = loader.get_template("404.html")
    return HttpResponseNotFound(
        t.render(RequestContext(request, {'request_path': request.path})))


def http500(request):
    t = loader.get_template("500.html")
    return HttpResponseServerError(
        t.render(RequestContext(request, {'request_path': request.path})))


def home(request):
    return render_to_response("index.html", 
                              context_instance=RequestContext(request))        
