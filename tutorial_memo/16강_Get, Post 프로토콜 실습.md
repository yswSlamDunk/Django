### Get과 Post의 차이점

* Get은 주소창에 입력하면 자동적으로 전달 되는 방식
* Post는 따로 설정이 필요함
  *  Post를 쓰기 위한 설정은 html 안에 Form을 만들어 줘야함



### Post

```html
{% extends 'base.html' %}

{% block content %}

    <div style = "height: 20rem; background-color: #38df81; border-radius: 1rem; margin: 2rem;">
        <h1>
            testing
        </h1>

        <form action = "/account/hello_world/" method = "post">
            {% csrf_token %}
            <input type = "submit" class = "btn btn-primary" value = "POST">
        </form>
    </div>
    
{% endblock %}
```

* form은 서버에게 보내는 요청명세서의 개념
  * 글이나 파일 등의 모든 데이터들이 post body 안에 들어가는데, 정확하게는 \<form\> tag안에 들어감
  * form tag 안에 action에는 요청을 하려는 url을 넣어줘야 함
  * form tag 안에 method에는 프로토콜 방식을 넣어줘야 함
* 특정 interaction이 존재해야 서버에 전달할 수 있음
  * interaction을 만들기 위해 input 버튼을 생성
    * input 버튼의 type은 submit으로 생성
    * 버튼의 모양(class)은 "btn btn-primary"로 생성
      * btn btn-primary는 학습 초기 html파일에서 head에서 입력한 bootstrap에 이씨는 버튼 클래스를 의미함
    * input 버튼에 들어가는 글씨는 value로 생성

* django에서 Post protocol 방식으로 서버에 요청을 보낼 때는 항상 csrf_token이라는 것을 form 안에다 명시를 해야함
  * csrf_token은 django에서 제공하는 보안기능 중 하나라고 생각하면 됨
* input 버튼을 만들고 Post protocol 방식으로 요청을 했지만, 보여지는 화면을 담당하는 view 단에서 post와 get 방식과 관련한 처리를 하지 않으면, 화면의 변화는 존재하지 않음
* view 에서 protocol 방식과 관련한 처리를 진행해야 함

```python
# accountappp/views.py

def hello_world(request):
    if request.method == 'post':
        return render(request, 'accountapp/hello_world.html', context = {'text' : 'POST METHOD!!!'})
    else :
        return render(request, 'hello_world.html', context = {'text' : 'GET METHOD!!!'})
```

* 만약 request의 protocol이 post일 경우, 기존의 방식과 같이 render를 통해 return을 진행하는데, 이때, context라는 부분에서 'text' 이름에 'POST METHOD!!!' 텍스트를 담아서 전달
  * context는 데이터 꾸러미의 개념으로 이해

```html
{% extends 'base.html' %}

{% block content %}

    <div style = "height: 20rem; background-color: #38df81; border-radius: 1rem; margin: 2rem;">
        <h1>
            testing
        </h1>

        <form action = "/account/hello_world/" method = "post">
            {% csrf_token %}
            <input type = "submit" class = "btn btn-primary" value = "POST">
        </form>
        
        <h1>
            {{ text }}
        </h1>
    </div>
    
{% endblock %}
```

* {{ text }} 
  *  text의 값이 존재한다면, 화면에 context 안에 text라는 이름의 데이터를 화면에 띄워줌
