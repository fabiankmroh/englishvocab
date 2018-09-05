from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Vocab

def index(request):
    rVocabL = Vocab.objects.order_by('-pub_date')[:5]
    template = loader.get_template('vocabs/index.html')
    context = {
        'rVocabL' : rVocabL,
    }
    return HttpResponse(template.render(context, request))

def vocab(request, vocab_id):
    return HttpResponse("Word: %s" % vocab_id)
