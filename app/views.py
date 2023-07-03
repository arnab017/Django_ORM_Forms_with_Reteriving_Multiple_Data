from django.shortcuts import render
from app.models import *
from django.db.models.functions import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def display_topic(request):
    topics = Topic.objects.all()
    
    d = {'topics': topics}
    return render(request,'dt.html',d)

def display_webpage(request):
    # webpages = Webpage.objects.all()
    
    d = {'webpages': webpages}
    return render(request,'dw.html',d)


def display_ar(request):
    ar = AccessRecord.objects.all()
    
    d = {'ar': ar}
    return render(request,'dar.html',d)

def display_all(request):
    
    topics = Topic.objects.all()
    webpages = Webpage.objects.all()
    ar = AccessRecord.objects.all()
    
    d = {'topics': topics, 'webpages': webpages, 'ar': ar}
    
    return render(request,'dall.html',d)

def display_form(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pw']
        print(username, password)
        return HttpResponse('<center><h3>Data Submitted Successfully</h3></center>')
    
    return render(request,'display_form.html')

def topic_form(request):
    if request.method == 'POST':
        topic = request.POST['tp']
        TO = Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        print(topic)
        return HttpResponse('<center><h3>Topic Successfully inserted</h3></center>')
    return render(request,'topic_form.html')

def webpage_form(request):
    LTO = Topic.objects.all()
    d = {'LTO': LTO}
    if request.method == 'POST':
        topic = request.POST['tp']
        name = request.POST['na']
        url = request.POST['ur']
        
        TO = Topic.objects.get(topic_name=topic)
        TO.save()
        WO = Webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        
        return HttpResponse('<center><h3>Webpage Successfully Created</h3></center>')
    return render(request,'webpage_form.html',d)

def ar_form(request):
    webpages = Webpage.objects.all()
    d = {'webpages': webpages}
    
    if request.method == 'POST':
        
        name = request.POST['na']
        date = request.POST['da']
        author = request.POST['au']

        WO = Webpage.objects.get(name=name)
        WO.save()
        AO = AccessRecord.objects.get_or_create(name=WO,date=date,author=author)[0]
        AO.save()

        return HttpResponse('<center><h3>AccessRecord Successfully inserted</h3></center>')
    return render(request,'ar_form.html',d)

def retrieve_Webpage(request):
    LTO = Topic.objects.all()
    d = {'LTO':LTO}
    if request.method == 'POST':
        RTO = request.POST.getlist('to')
        RWO = Webpage.objects.none()
        
        for i in RTO:
            RWO = RWO|Webpage.objects.filter(topic_name=i)
        
        wd = {'RWO':RWO}
        return render(request,'dw.html',wd)
    return render(request,'display_webpage.html',d)

def retrieve_AR(request):
    LWO = Webpage.objects.all()
    d = {'LWO':LWO}
    if request.method == 'POST':
        RWO = request.POST.getlist('to')
        RARO = AccessRecord.objects.none()
        
        for i in RWO:
            RARO = RARO|AccessRecord.objects.filter(name=i)
        
        acd = {'RARO':RARO}
        return render(request,'dar.html',acd)
    return render(request,'display_accessrecord.html',d)