from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.utils import timezone

from .models import Vocab

import random

def index(request):
    rVocabL = Vocab.objects.order_by('-pub_date')
    context = { 'rVocabL' : rVocabL }
    return render(request, 'vocab/index.html', context)

def insert(request):
    return render(request, 'vocab/insert.html')

def vocab_insert(request):
    Vocab.objects.create(vocabTxt=request.POST['vocab'],pub_date=timezone.now())

    rVocabL = Vocab.objects.order_by('-pub_date')
    context = { 'rVocabL': rVocabL}
    return render(request, 'vocab/index.html')

def detail(request, vocab_id):
    vocab = Vocab.objects.get(pk= vocab_id)
    vocabD = vocab.definition_set.all()

    return render(request, 'vocab/detail.html', {'vocab':vocab, 'definition_set': vocabD, 'vocab_id':vocab_id})

def detail_insert(request,vocab_id):
    return render(request, 'vocab/detail_insert.html',{'vocab_id':vocab_id})

def detail_insert_save(request, vocab_id):
    vocab = Vocab.objects.get(pk = vocab_id)
    vocab.definition_set.create(defTxt = request.POST['definition'], wrongC = 0)
    vocab.save()

    vocabD = vocab.definition_set.all()

    return render(request, 'vocab/detail.html', {'vocab':vocab, 'definition_set': vocabD, 'vocab_id':vocab_id})

def test_start(request):
    return render(request, 'vocab/test_start.html')

def test_form(request):
    Vpk = random.randint(1,len(Vocab.objects.all()))
    Dpk = 1
    vocab = Vocab.objects.get(pk = Vpk)
    definition = vocab.definition_set.filter(pk = Dpk)
    return render(request, 'vocab/test_form.html', {'definition':definition, 'Vpk':Vpk, 'Dpk':Dpk})

def test_submit(request, Vpk, Dpk):
    vocab = Vocab.objects.get(pk = Vpk)
    definition = vocab.definition_set.get(pk = Dpk)
    if(request.POST['vocab'] != vocab):
        definition.wrongC += 1
