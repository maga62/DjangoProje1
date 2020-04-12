
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
from home.models import Settings, ContactFormMessage, ContactFormu
from product.models import Product


def index(request):
    setting = Settings.objects.get(pk=1)
    sliderdata =Product.objects.all()[:4]
    context = {'setting': setting,
               'page':'home',
               'sliderdata':sliderdata}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslarimiz(request):
    setting = Settings.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email =form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "mesajiniz basarili bir sekilde gonderilmisdir")
            return HttpResponseRedirect('/iletisim')


    setting = Settings.objects.get(pk=1)
    form=ContactFormu()
    context = {'setting': setting, 'form':form}
    return render(request, 'iletisim.html', context)