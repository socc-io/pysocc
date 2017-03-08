# SOCC API Server (Python Flask)
##Requirements
* flask
* flask_login
* flask_admin
* flask_sqlalchemy
* SQLAlchemy
* sqlalchemy_utils

위의 모듈들을 설치해야한다.

### Database 연동

 /tmp/에 socc.db라는 이름으로(/tmp/socc.db 가 존재하도록) sqlite3 Database파일을 만들거나, [configure.py](app/configure.py) 에서 SQLALCHEMY_DATABASE_URI 변수를 설정해주어야 합니다.

유닉스의 경우 아래와 같이 쉘에서 실행시켜야 합니다.

```sh
sudo apt install sqlite3
sqlite3 /tmp/socc.db
```

윈도우의 경우 https://www.sqlite.org/ 에서 sqlite3를 받아 적당한 위치에 .db파일을 만들어, configure.py를 설정해야합니다.

## testment

```sh
pytest
```

## TODO

TODO는 기본적으로 Model을 중심으로 나열되어 있습니다. 각 항목은 항목명을 이름으로하는 Model을 다루는 Service, Controller전반에 대한 Task를 의미합니다.

각 항목의 완성도에 따른 체크 여부는 그 항목을 개발한 분의 주관으로 판단하셔도 됩니다. 각 모델에 대하여 기본적인 CRUD만 제대로 동작한다면 체크하셔도 될 것 같습니다.

TODO리스트는 Model중심으로 나열되어있습니다. 자식항목들이 있는 것은, 부모항목과 자식항목이 OneToMany Relation를 가지고 있음을 의미합니다.

OneToOne, ManyToMany를 TODO에서 표현하지 않았습니다. 세부 마크다운에서 확인해주세요.

- [x] [Study](md/TODO_Study.md) 
      - [x] [StudyIssue](md/TODO_StudyIssue.md)
      - [ ] StudyPlan
       - [ ] StudyPlanAttendance
- [x] Event
      - [ ] EventComment
- [x] User

## 기타

* None
