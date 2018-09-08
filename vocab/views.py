from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone

from .models import Vocab

def index(request):
    rVocabL = Vocab.objects.order_by('-pub_date')
    context = { 'rVocabL' : rVocabL }
    return render(request, 'vocab/index.html', context)

def detail(request, vocab_id):
    vocab = get_object_or_404(Vocab, pk = vocab_id)
    definition_set = vocab.definition_set.all()
    return render(request, 'vocab/detail.html', {'vocab':vocab, 'definition_set':definition_set})

def insert(request):
    return render(request, 'vocab/insert.html')

def vocab_insert(request):
    Vocab.objects.create(vocabTxt=request.POST['vocab'],pub_date=timezone.now())
    
    rVocabL = Vocab.objects.order_by('-pub_date')
    context = { 'rVocabL': rVocabL}
    return render(request, 'vocab/index.html',context)
