from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    if request.method == 'post':
        return render(request, 'hello_world.html', context = {'text' : 'POST METHOD!!!'})

    else:
        return render(request, 'hello_world.html', context = {'text' : 'GET METHOD!!!'})
