from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext=request.POST.get('text', 'default')
    isremovepunc=request.POST.get('removepunctuations', 'off')
    isfullcaps=request.POST.get('fullcaps', 'off')
    isnewlineremove=request.POST.get('newlineremover', 'off')
    isspaceremove=request.POST.get('removespace', 'off')
    ischarcount=request.POST.get('charactercount', 'off')
    purpose = ""

    if isremovepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + "| Remove Punctuations"
    
    if isfullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpose = purpose + " | Capitalize All"
    
    if isnewlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + " | Remove New Line"
    
    if isspaceremove == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if (not(index>len(djtext)) and not(djtext[index] == " " and djtext[index+1]==" ")):
                analyzed = analyzed + char
        
        djtext = analyzed
        purpose = purpose + " | Remove Extra Space"
    
    if ischarcount == 'on':
        counter = 0
        for char in djtext:
            if char != " ":
                counter += 1
        
        analyzed = analyzed + "\n\n\n\n\tCharacter Count: " + str(counter)
        purpose = purpose + " | Character Count"
    
    if isremovepunc != 'on' and isspaceremove != 'on' and ischarcount != 'on' and isnewlineremove != 'on' and isfullcaps != 'on':
        return HttpResponse("Error")
    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request,'analyze.html', params)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')