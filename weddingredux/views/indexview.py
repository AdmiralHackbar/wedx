__author__ = 'dgg1988'

from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template("index.html")
    context = RequestContext(request, {
        'page' : {
            'title' : "WAKAKAKAKAKAKA"
        }
    })
    return HttpResponse(template.render(context))