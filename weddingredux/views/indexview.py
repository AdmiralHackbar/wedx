__author__ = 'dgg1988'

from django.http import HttpResponse

def index(request):
    return HttpResponse("This will be the index view.")