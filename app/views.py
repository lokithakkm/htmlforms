from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *
def htmlforms(request):
    if request.method=='POST':
        n=request.POST['un']
        p=request.POST['pw']
        d={'n':n,'p':p}
        return render(request,'data.html',d)
    return render(request,'htmlforms.html')

def insert_topic(request):
    if request.method=='POST':  
        tn=request.POST['tn']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('Topic is inserted successfully go and check in admin if u want')
    return render(request,'insert_topic.html')
def insert_webpage(request):
    if request.method=='POST':  
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        w=Webpage.objects.get_or_create(topic_name=tn,name=na,url=ur)[0]
        w.save()
        return HttpResponse('Topic is inserted successfully go and check in admin if u want')
    
    return render(request,'insert_webpage.html')