# TODO: Study

스터디에 대한 기초적인 정보를 담는 모델입니다.

## Columns

| name         | type         | attribute  | comment     |
| ------------ | ------------ | ---------- | ----------- |
| id           | Integer      | PK         |             |
| name         | varchar(128) |            |             |
| created_date | datetime     |            |             |
| user_num     | Integer      | aggregated | count(user) |

## Relationships

| name   | model      | secondary       |
| ------ | ---------- | --------------- |
| users  | User       | user_study_conn |
| issues | StudyIssue |                 |

* User와 ManyToMany