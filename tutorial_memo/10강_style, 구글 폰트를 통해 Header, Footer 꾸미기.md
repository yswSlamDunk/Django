__지난 수업에서 진행했던, header, footer를 꾸미는 것이 이번 강의의 목표__

* 일단, 기존에 작업했던 header를 지우고 거기에 다시 작업을 함
* 이번 강좌를 통해 style 을 주는 방법을 학습함
* 부트스트랩 적용법 학습

* 폰트 적용



## header.html

```html
<div style = 'text-align : center; margin : 2rem 0 ;'>
    <div>
        <h1>Pragmatic</h1>
    </div>
    
    <div>
        <span>nav1</span>
        <span>nav2</span>
        <span>nav3</span>
        <span>nav4</span>
    </div>
</div>
```

* margin : 2rem 0

  * 이  style 명령어는 , 상하로 2rem margin을 주고, 좌우로 0 rem margin을 준다는 의미

    

### footer.html

```html
<div style = 'text-align : center; margin : 2rem 0 ;'>
    <div style = 'font-size : 0.6rem;'>
        <span>공지사항</span> |
        <span>제휴문의</span> |
        <span>서비스 소개</span> |
    </div>
    
    <div style = 'margin-top : 1rem;'>
        <h6 style = 'margin-top : 1rem;'>Pragmatic</h6>
    </div>
</div>
```



### 부트스트랩 

* 트위치에서 개발함
* base.html에서 head 부분에 부트스트랩 정보를 입력함 

```html
<html>
    <meta charset = 'UTF-8'>
    <Title> Pragmatic </Title>

    <!-- BOOTSTRAP -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</html>
```



### 주석달기

* html에서 주석을 다는 방법 : " ctrl + / "



### Fonts

* https://fonts.google.com/ 에서 폰트를 가져올 수 있음

```HTML
<html>
    <meta charset = 'UTF-8'>
    <Title> Pragmatic </Title>

    <!-- BOOTSTRAP -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <!-- GOOGLE FONTS LINK -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

</html>
```

* head.html 파일에 위의 사이트에서 마음에 드는 폰트의 정보를 가져와 입력

```html
<div style = "text-align : center; margin-bottom : 2rem 0; ">
    <div>
        <h1 style = "font-family: 'Lobster', cursive; ">Pragmatic</h1>
    </div>
    
    <div>
        <span>nav1</span>
        <span>nav2</span>
        <span>nav3</span>
        <span>nav4</span>
    </div>
</div>
```

* 후에 홈페이지에 입력된 사용방법을 참조하여 style에 추가로 입력한다.