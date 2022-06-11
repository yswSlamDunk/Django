# HTML

* H : Hyper
* T : Text
* M : Markup
* L : Language



# extends / include

* 둘의 차이에 대해서 학습 진행

* html을 가져온다는 점에서 유사하나 사용 용도가 다름

* extends
  * 바탕을 가져오는 느낌
* include
  * 내용을 가져오는 느낌

* Response View
  * extends로 바탕을 가져오고, include로 내용을 가져와, 요청의 응답에 해당하는 view를 만듬



# base.html 생성

* pragmatic/templetes/base.html 생성

  ```html
  <!DOCTYPE html>
  <html lang = "en" >
      <head>
          <meta charset = "UTF-8">
          <title> Title</title>
      </head>
      <body>
  
      </body>
  </html>
  ```

* accountapp에서 views.py에서 응답을 해줄 때, templetes/base.html을 가져오고 내용을 채워 응답할 예정

* 기존에 작업했던 아래의 코드는 Response를 직접 생성하는 코드

  ```python
  return HttpResponse('안녕하세요.')
  ```



# templetes 폴더 경로 설정

* pragmatic/settings.py에서 TEMPLATES 변수에서 설정 가능

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BAWSE_DIR, 'templates')], 
          # DIRS에 templates를 설정하면, 자동으로 해당 주소에서 templates를 찾음
          
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  