# File created by me
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello I am Aditya")
#
#
# def about(request):
#     return HttpResponse('''<h1>About myself</h1> <a href = 'https://www.linkedin.com/in/adityakulshrestha02'> This is
#     my linkedin page</a>''')

# def index(request):
#     return HttpResponse("Home")
# def index(request):
#     param = {'name': 'tatya_bichu', 'place': 'chamariyana mohalla'}
#     return render(request, 'index.html', param)
def index(request):
    return render(request, 'index.html')


def removepunc(request):
    print(request.GET.get('text','The user has not input any string'))
    return HttpResponse("Remove punc")


def capfirst(request):
    return HttpResponse("capitalize first")


def newlineremove(request):
    return HttpResponse("Capitalize first")


def spaceremove(request):
    return HttpResponse("Space Remove <a href = "'./'"> Here return back to home page</a>")


def charcount(request):
    return HttpResponse("Char Counter")


def analyze(request):
    mytext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc','off')  #default value is off
    fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')

    # Check checkbox values
    if removepunc == "on":
        punctuations = '''!()-[]{}:;'"/\,<>.?@#$%^&*!~`_'''
        analyzed = ''
        for char in mytext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuations', 'analyzed_text': analyzed}
    # return HttpResponse("remove punc")
        return render(request,'analyze.html',params)

    # if fullcaps is on
    elif (fullcaps=='on'):
        analyzed = mytext.upper()
        params = {'purpose':'Change to uppercase', 'analyzed_text': analyzed}
        return render(request,'analyze.html',params)


    elif (newlineremover=='on'):
        analyzed = ""
        for char in mytext:
            if char!= '\n':
                analyzed = analyzed + analyzed

        params = {'purpose':'Removed Newline','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)


    elif (extraspaceremover=='on'):
        analyzed = ""
        for index,char in enumerate(mytext):
            if not (mytext[index]== ' ' and mytext[index+1]==" "):
                analyzed += char

        params = {'purpose':'Removed Newline','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)


    else:
        return HttpResponse("Error")

