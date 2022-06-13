# Model

* django에서 model 이란 database와 django 내부에서 사용이 편하도록 연동을 해주는 역할을 함
* db의 내용을 자세히 알지 않아도 된다는 장점 존재



## accountapp/model.py

* accountapp의 중간 부분을 동적으로 표시하게 만들 예정인데, 중간 부분의 내용을 DB와 연동하여 채울 수 있도록 할 예정

```python
from django.db import models

class Hello_world(models.Model):
    text = models.CharField(max_length = 255, null = False)
    
```

* models.CharField는 문자열을 저장하는 공간
* null = False는 null이면 안된다는 것을 의미
* max_length는 문자열 최대 길이를 의미



### python manage.py  makemigrations

* model.py에서 쓰는 내용을 db와 연동시킬 수 있는 파일로 만들어 주는 작업을 함
* 위의 shell을 실행하면, Migrations for 'accountapp'; : accountapp/migrations/0001_initial.py -Create model HelloWorld 라는 글자가 나타나는데, 해당 경로로 이동하면 출력문과 동일한 파일이 생성됨
* accountapp/migrations/0001_initial.py 파일은 임의로 지우지 말고 보관하길 권장 : 임의로 지울 경우, 복잡한 문제가 발생할 수 있음
* 생성된 파일의 내용은 이해할 필요는 없음
* 해당 내용은 model.py에 있는 내용에 맞게 db와 django를 연결해주는 역할을 함



### python manage.py migrate

* 위의 shell을 실행해야 db와 django가 연결됨
* python manage.py makemigrations는 연결을 위해 필요한 파일을 생성하는 역할

* pragmatic/settings.py에 setting.py에 보면 DATABASE 관련 설정을 확인할 수 있음
  * 나중에는 DATABASE의 종류를 변경할 예정