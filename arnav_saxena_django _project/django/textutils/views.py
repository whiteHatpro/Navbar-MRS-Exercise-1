#i have created his file-arnav
from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request, 'index.html')
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)
    if(removepunc == "on"):
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
             analyzed = analyzed + char.upper()
        params={'purpose':'CAPITALIZED TEXT', 'analyzed_text': analyzed}
        djtext=analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params={'purpose':'New Line Remover', 'analyzed_text': analyzed}
        djtext=analyzed
    if(charcount == "on"):
        count = 0
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "):
                count = count + 1
        analyzed=count
        params={'purpose':'Character Counter', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params={'purpose':'New Line Remover', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and spaceremover != "on" and newlineremover != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("ERROR !!, please select any operation and try again")
    return render(request, 'analyze.html', params)    