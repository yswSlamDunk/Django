from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from pragmatic.accountapp.models import HelloWorld


def hello_wold(request):
    if request.method == 'post':
        tmp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse('accountapp : hello_world'))
                                                              
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'hello_world.html', context = {'hello_world_list' : hello_world_list})
