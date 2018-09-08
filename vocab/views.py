from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Vocab

def index(request):
    rVocabL = Vocab.objects.order_by('-pub_date')[:5]
    context = { 'rVocabL' : rVocabL }
    return render(request, 'vocab/index.html', context)

def detail(request, vocab_id):
    vocab = get_object_or_404(Vocab, pk = vocab_id)
    return render(request, 'vocab/detail.html', {'vocab':vocab})
