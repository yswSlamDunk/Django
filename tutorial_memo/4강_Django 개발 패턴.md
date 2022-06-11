# MVC

* M : model

* V : view

* T : template
  * 원래는 C : controller가 맞으나 django 에서는 template로 씀
  * 개발 패턴 및 역할은 거의 동일함
* model, view, template가 각자의 역할을 하며 전체적인 프레임워크를 구성함



### Model

* Model은 Database와  통신을 해주게 하는 편리한 도구
* 예시
  * 만약 신규 유저가 회원가입을 진행하면, 하나의 유저 객체가 생성됨
  * 하나의 유저가 새로운 글을 적으면 하나의 글 객체가 생성됨
  * 이렇게 생성된 유저, 글 객체를 database에 저장을 해야 함
  * 저장하는 과정에서 db쪽 언어를 사용하지 않고 원활하게 저장, 검색 등등을 할 수 있게 해주는 것이 Model의 역할
* database
  * database는 행(row)와 열(columns)로 구성됨
  * 예시
    * 하나의 게시글(article)은 여러 개의 속성(title, article_context, image ...)으로 구성됨
    * 데이터베이스에선 하나의 게시글(article)은  row, 여러 개의 속성들은 columns로 저장됨

* 모델을 설정만 하면 위의 내용들을 자동으로 할 수 있게 됨
* db에 대해서 생각을 덜 할 수 있음



### View

* django에서 계산과 관련된 모든 부분을 담당하는 역할
* 요청과 응답을 담당함
* 예시
  * 유저가 서버에 어떤 요청을 함
  * 서버는 그 응답에 대답하기 위해서 아래의 예시와 같은 행위를 함
    * check if authenticated : 권한이 있는지
    * check request valid : 유효한 요구인지
    * collect data from DB : DB에서 데이터 검색 및 가져오기
    * render response :  응답을 만들기



### Template

* 실질적으로 우리의 눈에 볼 수 있는 것들과 밀접한 관련이 있음
  * javascript, html, css 
* User Interface 내부(화면)에 있는 내용들을 어떻게 생성해낼 것인가와 관련이 있음
* 예시
  * 유저는 특정 게시글을 보고 싶음(요청을 보냄)
  * 서버에서 앞서 언급된 작업들을 작업하고, 요청에 부합되는 article을 전달함
  * article은 html, javascript, css로 구성되어 있는데 이것들로 눈에 보여지는 화면을 만드는 역할을 Template가 함