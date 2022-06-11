# accountapp 생성

```shell
!python manage.py startapp "app이름 //이건 accountapp으로 생성했었음"
```

* 기존에 pragmatic이라는 main app을 생성했음

* 위의 명령어를 통해 생성한 새로운 accountapp을 생성함

* pragmatic/settings.py : 프로젝트의 setting을 관리할 수 있는 파일

* settings.py에는 INSTALLED_APPS 변수가 존재함

* INSTALLED_APPS에 accountapp을 추가해야함

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'accountapp'
  ]
  ```

  

# accountapp에서 화면 생성

* 브라우저에서 어떤 경로로 들어오면 hello world를 출력하는 view를 만들 예정

* account_app에서 view.py

  ```python
  from django.http import HttpResponse
  
  def hello_world(request):
  	return HttpResponse('Hello world')
  ```

  * 위의 과정으로 view를 만들었고, 추가작업으로 routing 해주는 과정이 필요함
  * 특정 주소로 와야 위에 만든 view를 보여줄 수 있는데, 특정 주소와 view를 연결해주는 과정이 필요



# 생성한 view와 특정 주소를 연결해주는 routing 작업

* pragmatic 폴더는 제일 중요한 rout app이라 제일 먼저 요청을 받는 앱임

* pragmatic/urls.py에서 라우팅을 진행

  ```python
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls), # 기본으로 설정이 되어있는 view
      path('account/', include('accountapp.urls'))	# 생성한 view와 연결
  ]
  ```

  * account/ : account 앱 내부에 있는 view에 접근하기 때문에 "/"를 꼭 써야함
  * include(): account 내부에 있는 urls.py를 모두 포함해, 하위 directory에 분기를 해하 하는 의미



# accountapp/urls.py

```python
from django.urls import path
from account.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world')
]
```

