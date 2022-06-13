# CSS

* C : cascading
* S : style
* S : sheet



# DISPLAY attribute

```html
<h1>
    
</h1>
```

* 이런 tag들 마다 display attribute가 존재함



### Block

* 모든 tag에는 부모가 존재함

  ```html
  <div>
      <h1>
        오드리햅번  
      </h1>
  </div>
  ```

  * 위의 코드에선 h1 tag의 부모 tag는 div tag임
  * block은 부모 tag의 최대한의 너비를 가져가는 속성



### Inline

* 만약 글자가 있다면, 글자의 높이 만큼만 가져감
* 한 줄에 여러 개의 Inline이 쌓임



### Inline-block

* block임에도 불구하고 inline의 성격을 가짐
* 한 줄에 여러 개가 쌓임



### None

* 있긴 있지만 보이지 않음

* Visibility 속성에 hidden이 있는데, 이는 보이지는 않을 뿐이지 존재하는 속성이다
* hidden은 보이지 않을 뿐이지 자리는 차지하고 있지만, None 속성은 자리도 차지하지 않음



# Size Attribute

* px
* em
* rem
* %
* size attirbute는 기초 font-size에 관련이 있다
  * 기초 font-size에 반응하여 크기가 변하는 것도 있고, 변하지 않는 것도 있음
  * 휴대폰 화면의 기초 font-size와 컴퓨터 브라우져에서의 기초 font-size는 차이가 있음
  * __Responsive__ : 반응형 
    * 기초 font-size에 따라 크기가 변하는 것이 중요한 이유는 반응형 웹을 만들기 때문
    * 반응형으로 만든다는 것은 desktop, phone 등의 화면에 반응해 크기가 자동으로 조절된다는 의미



### px

* 부모가 커지든, 작아지든 상관 없이 크기가 일정함
* parent의 font-size가 변하든 상관 없이 크기가 일정함



### em

* 부모가 커지면 같이 커짐
  * ex) 부모 1.5x -> 자식 1.5x
* em을 잘 쓰지 않는 이유는 부모의 부모가 커지면 연쇄적으로 커지기 때문
  * ex) 부모 2x -> 부모 2x =>> 4x



### rem

* 거의 모든 곳에서 rem을 사용 함
* 1rem은 16px
* root HTML에 기본적으로 default font-size가 존재(16px)
* rem은 default font-size에 비례하여 크기가 조절됨
* 부모의 크기가 커지든 작아지든 자식의 크기는 동일함
* 하지만 html의 default font-size가 커지면 모두 커짐



### %

* 부모의 %에 해당하는 부분을 차지
* rem 다음으로 사용을 많이 함

