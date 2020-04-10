
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Settings


def index(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting,'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting,}
    return render(request, 'hakkimizda.html', context)

def referanslarimiz(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting,}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting,}
    return render(request, 'iletisim.html', context)