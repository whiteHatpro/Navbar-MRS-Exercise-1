
# Views.py
# I have created this file - Vansh Motwani
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed

    if (newlineremover == "on"):
        str=list(djtext.split("\n"))
        a=''
        for e in str:
            a=a+e
        str=list(a.split("\r"))
        b=''
        for e in str:
            b=b+e
        djtext=b
    if(removepunc == "off" and fullcaps=="off" and newlineremover == "off" and extraspaceremover=="off"):
        return HttpResponse("Error")
    print(djtext)
    params = {'purpose':'', 'analyzed_text': djtext}
    return render(request, 'analyze.html', params)

