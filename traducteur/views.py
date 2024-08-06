from django.shortcuts import render , HttpResponse
from translate import Translator

def traducteur(request):
    
    if request.method == "POST" :
        text = request.POST["traducteur"]
        langue = request.POST["language"]
        translator = Translator(to_lang=langue)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request , "acceuil.html")
        
        


# Create your views here.
