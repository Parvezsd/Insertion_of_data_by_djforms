from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=request.POST['tn']

            TO=Topic.objects.get_or_create(topic_name=tn)
            return HttpResponse('Topic is Created')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    d={'EWFO':WebpageForm()}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=request.POST['tn']
            n=request.POST['n']
            url=request.POST['url']
            email=request.POST['email']
            TO=Topic.objects.get(topic_name=tn)
            WP=Webpage.objects.get_or_create(topic_name=TO,name=n,email=email,url=url)
            return HttpResponse('Webpage is Created')
        else:
            return HttpResponse('Invalid data')
        

    return render(request,'insert_webpage.html',d)

def insert_access(request):
    d={'EAFO':AccessRecordForm()}
    if request.method=='POST':
        ARFDO=AccessRecordForm(request.POST)
        if ARFDO.is_valid():
            # tn=request.POST['tn']
            n=request.POST['n']
            d=request.POST['d']
            a=request.POST['a']
            WP=Webpage.objects.get(id=n)
            AR=AccessRecord.objects.get_or_create(name=WP,date=d,author=a)
            return HttpResponse('Access Record is Created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_access.html',d)    

