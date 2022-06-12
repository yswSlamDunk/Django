## base.html head

* 후에 base.html에서 head에서 링크를 가져오거나, 소스를 가져오는 등 여러 가지 작업이 진행될 예정
* 앞으로의 작업을 고려, html의 head에 관련된 부분을 tmplete 폴더에 따로 생성

* 만약 head와 관련된 부부을 따로 생성하지 않는다면, 매우 복잡하게코드가 정리됨
* head 관련 부분을 따로 생성하고 include로 가져와 쓰는 방식으로 진행



__templetes/head.html__

```html
<html>
   	<meta charset = 'UTF-8'>
    <Title> Title </Title>
</html>
```



__templets/base.html__

```html
<!DOTYPE html>
<html lang="ko">
    {% include 'head.html %'}
    
    <body>
        Hello world!
    </body>
</html>
```

* head.html을 생성한 후, base.html에서 head.html을  include 해야 함



## base.html에서 div를 통한 화면 3분할

```html
<body>
   	<divstyle = "height: 10rem; background-color: #38df81; border-radius: 1rem; margin: 2rem">
            
        </div>

        <divstyle = "height: 10rem; background-color: #38df81; border-radius: 1rem; margin: 2rem">

        </div>

        <divstyle = "height: 10rem; background-color: #38df81; border-radius: 1rem; margin: 2rem">

        </div>
</body>
```

* border-radius: 1rem : 마무리를 둥글게 표현하는 것
* margin: 요소들을 띄어놓는 것
* 현재 3분활된 모습을 나타내고 있는데, 처음과 마지막의 경우는 똑같은 모양을 유지하기 때문에, 해당 부분을 위한 html을 생성하고 동일하게 include를 통해 가져와서 사용하는 방식으로 진행



##  3분활 중 첫 번째(header), 세 번째(footer) 부분 html 생성

__header.html__

```html
<div style = "height: 10rem; background-color: #38df81; border-radius: 1rem; margin: 2rem">
            
</div>
```

__footer.html__

```html
<div style = "height: 10rem; background-color: #38df81; border-radius: 1rem; margin: 2rem">
    
</div>
```



## base.html의 body에서 두 번째 부분

* base.html의 body에서 두 번째 부분은 extend를 사용할 예정
* 이 부분은 내용이 변하는 부분
* extend를 사용하기 위해선 block 구문을 사용해야함

```html
<body>
    {% include 'header.html' %}
    {% block content %}
    {% endblock %}
</body>
```

* {% block content %}  :  content 이름의 block을 생성
* {% endblock %} : block이 끝나는 점을 나타내는 코드
* content 부분을 제외하고 기본적으로 중복이 되는 부분은 재활용할 수 있게 됨

​                                                                                                                    



### templetes/accountapp에서 hello_world.html 부분 문제 존재

```python
from djaongo.shortcuts import render

def hello_world(request):
    return render(request, 'accountapp/helloworld.html')
```

* 여기서 문제가 있음

```
TemplateDoesNotExist at /account/hello_world/
accountapp/helloworld.html
Request Method:	GET
Request URL:	http://127.0.0.1:8000/account/hello_world/
Django Version:	3.2.5
Exception Type:	TemplateDoesNotExist
Exception Value:	
accountapp/helloworld.html
Exception Location:	/home/yooseungwoo/anaconda3/envs/practice_django/lib/python3.10/site-packages/django/template/loader.py, line 19, in get_template
Python Executable:	/home/yooseungwoo/anaconda3/envs/practice_django/bin/python
Python Version:	3.10.4
Python Path:	
['/home/yooseungwoo/Desktop/Project/Django/pragmatic',
 '/home/yooseungwoo/anaconda3/envs/practice_django/lib/python310.zip',
 '/home/yooseungwoo/anaconda3/envs/practice_django/lib/python3.10',
 '/home/yooseungwoo/anaconda3/envs/practice_django/lib/python3.10/lib-dynload',
 '/home/yooseungwoo/anaconda3/envs/practice_django/lib/python3.10/site-packages']
Server time:	Sun, 12 Jun 2022 06:55:39 +0000
```

내 생각에는 urls.py나 이런 부분에서 경로를 설정하는 과정에 문제가 존재하는거 같음



