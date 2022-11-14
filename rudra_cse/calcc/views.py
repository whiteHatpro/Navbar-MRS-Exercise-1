import http.client
from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
from .models import tt

# Create your views here.

def home(request):
    int1=tt()
    int1.some='CHANGE IN UPPER CASE'
    int1.name='upper'
    int2=tt()
    int2.some='REMOVE ALL NEW LINES'
    int2.name='nlr'
    int3=tt()
    int3.some='REMOVE ALL PUNCTUATIONS'
    int3.name='pun'
    int4=tt()
    int4.some='REMOVE ALL SPACES'
    int4.name='space'

    int=[int1,int2,int3,int4]
    return render(request,'ghar.html',{'int':int})
    # return render(request,'ghar.html',{'name':'bh'})
    # return HttpResponse("heyy")
def add(request):
    a1=request.POST['text']
    uu=request.POST.get('upper','off')
    ll=request.POST.get('nlr','off')
    pun=request.POST.get('pun','off')
    sp=request.POST.get('space','off')
    w=False
    a2=''
    i=0
    if(uu=='on'):
        a1=a1.upper()
        i=i+1
    if (pun=='on'):
        for tes in a1:
            if (tes>='a' and tes<='z') or (tes==" ") or (tes=="\n") or (tes>='A' and tes<='Z')or(tes>='0'and tes<='9')or(tes=='-')or(tes=='+')or (tes=='='):
                 a2=a2+tes
        a1=a2
        a2=''
        i=i+1
    if(ll=='on'):
        for tes in a1:
            if tes!="\n":
                a2=a2+tes
        a1=a2
        a2=''
        w=True
        i=i+1
    if(sp=='on'):
        n=len(a1)
        for i in range(n-1):
            if a1[i]==" " and a1[i+1]==" " :
                pass
            else:
                a2=a2+a1[i]
        a1=a2
        i=i+1
    if i>0:
        res=a1
    else:
        res='please select a task to perform on your input='+a1
    return render(request,'result.html',{'res':res,'w':w})