### 이번 강의 학습 목표

1. Send Post data
2. Receive Post data
3. Save DB



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
                {% if hello_world_output %}
                <h1>
                    {{ hello_world_output.text }}
                </h1>
                {% endif %}
        
    </div>

{% endblock %}
```

* \<style = "font-family: 'lobster', cursive;" \>
  * 'lobster' font를 우선 사용하는데, 만약 존재하지 않으면, cursive를 사용
* \<input type = "text" name = "hello_world_input"\> 
  * 데이터를 입력하는 입력 type은 text
  * 서버에서 post protocol로 데이터가 전달 되었을 때, 데이터의 구별을 위해 데이터에 이름을 붙여줄 수 있는데 그 방법이 name이고, 여기선 hello_world_input 이름으로 설정



### accountapp/views.py

```python
def hello_wold(request):
    if request.method == 'post':
        tmp = request.POST.get('hello_world_input')
        new_hello_world = Hello_world()
        new_hello_world.text = tmp
        new_hello_world.save()
        
        return render(request, 'hello_world.html', context = {'hello_world_output' : new_hello_world'})
                                                              
	else :
		return render(request, 'hello_world.html', context = {'text' : 'GET METHOD!!!'})
```

* tmp = request.POST.get('hello_world_input')

  * request에서 POST 방식 중, hello_world_input 이라는 이름의 데이터를 가져와라 라는 명령어

* new_hello_world = Hello_world()

  * 여기에서 Hello_world는 accountapp/models.py에 선언한 class

  * text라는 이름의 CharField를 가짐

* new_hello_world.text = tmp

  * Hello_world라는 class는 text라는 CharField를 가지는데 여기에 request.POST.get('hello_world_input')을 통해 받은 내용을 할당

* new_hello_world.save()

  * database에 저장하는 과정