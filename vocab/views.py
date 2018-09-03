from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('At vocab index')

def vocab(request, vocab_id):
    return HttpResponse("Word: %s" % vocab_id)
