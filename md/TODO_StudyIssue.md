# TODO: StudyIssue

스터디에 관련된 게시글의 정보를 담습니다.

## Columns

| name     | type    | attribute    | comment |
| -------- | ------- | ------------ | ------- |
| id       | Integer | PK           |         |
| study_id | Integer | FK(study.id) |         |
| title    | Text    |              |         |
| content  | Text    |              |         |

## Relationships

| name  | model | secondary |
| ----- | ----- | --------- |
| study | Study |           |

