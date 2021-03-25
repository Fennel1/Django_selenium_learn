from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # pass
    # rerturn HttpResponse()
    # return HttpResponse('<html>')
    return HttpResponse('<html><title>To-Do lists</title></html>')
