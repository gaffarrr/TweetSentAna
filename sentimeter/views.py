from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
import sentimeter
from .sentimeter import primary

def index(request):
    user_input = userinput()
    return render(request, 'index.html', {'input_hashtag': user_input})

def analyze(request):
    user_input =userinput(request.GET or None)
    if request.GET and user_input.is_valid() :
        input_hashtag = user_input.cleaned_data['q']
        print (input_hashtag)
        data = sentimeter.sentimeter.primary(input_hashtag)
        return render(request, 'result.html', {'data': data})
    return render(request, 'index.html', {'input_hashtag': user_input})