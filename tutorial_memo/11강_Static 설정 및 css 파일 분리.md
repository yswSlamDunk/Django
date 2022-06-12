### CSS 파일 분리

```html
<h1 style = "text-align : center">
   	css 파일 분리
</h1>>
```

* 일반적으로 개발을 할 때, 기존에 style을 주기 위해서 위의 코드와 같이 직접 style 값을 입력하는 것이 아닌, css 파일을 만들어 관리함 

* css 파일을 분리하기 전 static에 관한 설정을 먼저 진행해야 함
* static은 정적을 뜻하는데, css, javascript, font 등 자주 변하지 않는 것들을 static이라 부름
* 이러한 static을 app 마다 관리를 하게 됨





## static 분리

* pragmatic/settings.py에서 STATIC_ROOT를 설정

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

```shell
python manage.py collectstatic
```

* 모든 static file을 모아주는 명령어로, 위에 설정한 STATIC_ROOT는 위의 shell 명령어로 모아지는 static file의 경로를 나타냄



__app에 종속되어 있지 않은 static_files__

* 일반적으로 static files는 app에 종속되어 만드는데, 모든 앱에 공통인 static_files를 관리하기 위한 경로를 생성
* pragmatic/settings.py에 설정

``` python
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

* pragmatic/static/base.css 생성

  * footer.html에서 Pragmatic 글자 관련 style 수정

  ```html
  <div style = 'text-align : center; margin : 2rem 0 ;'>
      <div style = 'font-size : 0.6rem;'>
          <span>공지사항</span> |
          <span>제휴문의</span> |
          <span>서비스 소개</span> |
      </div>
      
      <div style = 'margin-top : 1rem;'>
          <h6 class = "pragmatic_footer_logo">Pragmatic</h6>
      </div>
  </div>
  ```

  * style은 미리 생성한 style을 사용할 수 있도록 하기 위해서 아래와 같은 것을 진행함