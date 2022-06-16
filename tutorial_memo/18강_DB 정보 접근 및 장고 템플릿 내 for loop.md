### 학습목표

* 기존의 DB에 저장된 정보들을 긁어와서 화면에 나타내는 것



### accountapp/views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

from pragmatic.accountapp.models import Helloworld


def hello_wold(request):
    if request.method == 'post':
        tmp = request.POST.get('hello_world_input')
        new_hello_world = Helloworld()
        new_hello_world.text = tmp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        
        return render(request, 'hello_world.html', context = {'hello_world_list' : hello_world_list})
                                                              
    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'hello_world.html', context = {'hello_world_list' : hello_world_list})
```

* hello_world_list = Helloworld.objects.all()
  * db HelloWorld에 저장된 모든 객체를 가져오는 것을 의미
  * 여러 개의 객체의 모음



### hello_world.html

```html
{% extends 'base.html' %}

{% block content %}

    <div style = "border-radius: 1rem; margin: 2rem; text-align: center">
        <h1 style = "font-family: 'lobster', cursive;">
            Hello World LIST!!!
        </h1>

        <form action = "/account/hello_world/" method = "post">
            {% csrf_token %}
            <div>
                <input type = "text" name = "hello_world_input">
            </div>
            <input type = "submit" class = "btn btn-primary" value = "POST">

        </form>
            {% if hello_world_list %}
                {% for hello_world in hello_world_list %}
                    <h4>
                        {{ hello_world.text }}
                    </h4>
                {% endfor %}
            {% endif %}
        
    </div>

{% endblock %}
```

* {% if hello_world_list %} 
  * hello_world_list가 존재하면
* {% for hello_world in hello_world_list %}
  * hello_world_list의 객체를 하나씩 꺼냄
* 그런데 위의 코드에서 f5를 눌러 새로고침을 진행하면, 기존에 있었던 데이터가 반복적으로 나타나게 됨
  * 그 이유는 views.py를 보면	

```python
else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'hello_world.html', context = {'hello_world_list' : hello_world_list})
```

* 아래의 코드와 같이 get(post가 아닌) 방식에서 hello_world_list를 return 하기 때문

* 이러한 문제를 해결하기 위해, post를 한 후, get으로 돌아가서 같은 작업을 반복하지 않게 만들 예정

  * 새로고침 했을 때, render를 반복하지 않게 만든다는 의미

  * HttpResponseRedirect() 를 통해 진행할 예정

    

### accountapp/view.py

```python
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

```

* reverse() 공부 필요