from django.shortcuts import render
from django.http import HttpResponse

from pragmatic.accountapp.models import Hello_world


def hello_world(request):
    if request.method == 'post':
        tmp = request.POST.get('hello_world_input')

        new_hello_world = Hello_world()

        return render(request, 'hello_world.html', context = {'text' : tmp})

    else:
        return render(request, 'hello_world.html', context = {'text' : 'GET METHOD!!!'})
