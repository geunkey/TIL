[TOC]

# SQL with django ORM

## 기본 준비 사항

* django app

  * 가상환경 세팅

  * 패키지 설치

  * migrate

    ```bash
    $ python manage.py migrate
    ```
  
* 제공 받은 `users.csv` 파일은 db.sqlite3와 같은 곳에 위치하도록 이동

* `db.sqlite3` 활용

  * `sqlite3`  실행

    ```bash
    $ sqlite3 db.sqlite3
    ```

  * 테이블 확인

    ```sqlite
    sqlite > .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            auth_user_user_permissions  
    users_user
    ```
    
  * csv 파일 data 로드 및 확인

    ```sqlite
    sqlite > .mode csv
    sqlite > .import users.csv users_user
    
    sqlite > SELECT COUNT(*) FROM users_user;
    100
    ```



---



## 문제

> ORM은 django extensions의 shell_plus에서,
>
> SQL은 수업에서 진행한 [SQLite 확장프로그램](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) 사용 방식으로 진행

### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   User.objects.all()
   ```

      ```sql
   -- sql 대소문자 구별하지 않는다
   SELECT * FROM users_user; 
      ```

2. user 레코드 생성

   ```python
   # orm
   User.objects.create(first_name='근호', last_name='김', age='27', country='전라남도', phone='010-2731-2243', balance='123456789')
   ```

   ```sql
   -- sql
   insert into users_user (first_name, last_name, age, country, phone, balance) values ('근호', '김', 27, '전라남도', '010-2731-2243', 123456789);
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `102` 번 id의 전체 레코드 조회

   ```python
   # orm
   User.objects.get(pk=102)
   ```

   ```sql
   -- sql
   SELECT * FROM users_user where id=102;
   ```

4. 해당 user 레코드 수정

   - ORM: `102` 번 글의 `last_name` 을 '김' 으로 수정
   - SQL: `102` 번 글의 `first_name` 을 '철수' 로 수정

   ```python
   # orm
   user = User.objects.get(pk=102)
   user.last_name = '김'
   user.save()
   ```

      ```sql
   -- sql
   update users_user set first_name='철수' where id=102;
      ```

5. 해당 user 레코드 삭제

   - ORM: `102` 번 글 삭제
   - `SQL`:  `101` 번 글 삭제 

   ```python
   # orm
   user = User.objects.get(pk=101)
   user.delete()
   ```
   
   ```sql
   -- sql
   DELETE FROM USERS_USER WHERE ID=102;
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   User.objects.count()
   또는
   len(User.objects.all())
   ```

   ```sql
   -- sql
   SELECT COUNT(*) FROM USERS_USER;
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   User.objects.filter(age=30)
   
   User.objects.filter(age=30).values('first_name')
   ```

      ```sql
   -- sql
   select first_name from users_user where age=30;
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte`(이상) , `__lte` (이하), `__gt`(초과) `__lt`(미만) -> 대소관계 활용

   ```python
   # orm
   User.objects.filter(age__gte=30).count()
   ```

      ```sql
   -- sql
    select count(*) from users_user where age>=30;
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
    User.objects.filter(age__lte=30).count()
   ```

   ```sql
   -- sql
   select count(*) from users_user where age<=30;
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   User.objects.filter(age=30, last_name='김').count()
   
   User.objects.filter(Q(age=30) & Q(last_name='김')).count()
   ```

      ```sql
   -- sql
   select count(*) from users_user where age=30 and last_name='김';
      ```
   
6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   User.objects.filter(age=30)|User.objects.filter(last_name='김')
       
   
   # 사람 수    
   User.objects.filter(Q(age=30) | Q(last_name='김')).count()
   ```

   ```sql
   -- sql
   select * from users_user where age=30 or last_name='김';
   
   # 사람 수
   select count(*) from users_user where age=30 or last_name='김';
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   User.objects.filter(phone__startswith='02-').count()
   ```

      ```sql
   -- sql
   select count(*) from users_user where phone like '02-%';
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   User.objects.filter(country="강원도", last_name="황").values('first_name')
   ```
   
      ```sql
   -- sql
   select first_name from users_user where country = '강원도' and last_name = '황';
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('-age')[:10]
   ```

      ```sql
   -- sql
   select * from users_user order by age desc limit 10;
   
   # 나이가 많은 사람순 휴대폰 번호
   select phone from users_user order by age desc limit 10;
   
   많음 desc 내림차순
   적음 asc 오름차순
      ```

2. 잔액이 적은 사람순으로 10명

   ```python
   # orm
   User.objects.order_by('balance')[:10]
   ```

      ```sql
   -- sql
   SELECT * FROM users_user ORDER BY balance ASC LIMIT 10;
   
   # 잔액이 적은 사람 10명의 지역
   SELECT country FROM users_user ORDER BY balance ASC LIMIT 10;
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   User.objects.order_by('balance', '-age')[:10]
   ```
   
   ```sql
   -- sql
   select * from users_user order by balance, age DESC limit 10;
   
   select * from users_user order by balance asc, age DESC limit 10;
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   User.objects.order_by('-last_name', '-first_name')[4]
   ```
   
      ```sql
   -- sql
   select * from users_user order by last_name desc, first_name desc limit 1 offset 4;
   
   #1개만 뽑고 4번째부터 시작
      ```



---



### 4. 표현식

#### 4.1 Aggregate

> - https://docs.djangoproject.com/en/3.2/topics/db/aggregation/#aggregation
>- '종합', '집합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용
>- `Django_aggregation.md` 문서 참고

1. 전체 평균 나이

   ```python
   # orm
   User.objects.aggregate(Avg('age'))
   ```

      ```sql
   -- sql
   select AVG(age) from users_user;
   
   # AVG 대소문자 구별 안함. **하지만 ORM할땐 첫 글자는 무조건 대문자**(주의)
      ```

2. 김씨의 평균 나이

   ```python
   # orm
   #평균값 구할 때
   User.objects.filter(last_name='김').aggregate(Avg('age'))
   
   #최대값 구할 때
   User.objects.filter(last_name='김').aggregate(Max('age'))
   ```

      ```sql
   -- sql
   select AVG(age) from users_user where last_name='김';
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   User.objects.filter(country='강원도').aggregate(Avg('balance'))
   ```

   ```sql
   -- sql
   select avg(balance) from users_user where country = '강원도';
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   User.objects.aggregate(Max('balance'))
   ```

      ```sql
   -- sql
   select max(balance) from users_user;
   
   SELECT BALANCE FROM USERS_USER ORDER BY BALANCE DESC LIMIT 1;
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   User.objects.aggregate(Sum('balance'))
   ```
   
      ```sql
   -- sql
   select sum(balance) from users_user;
      ```



#### 4.2 Annotate

1. 지역별 인원 수

   ```PYTHON
   # orm
   User.objects.values('country').annotate(Count('country'))
   
   
   User.objects.values('country').annotate(num=Count('country'), a=Avg('balance'))
   
   
   # last_name 인원수
   User.objects.values('last_name').annotate(Count('last_name'))
   ```
   
   ```SQL
   -- sql
   SELECT COUNTRY, COUNT(*) FROM USERS_USER GROUP BY COUNTRY;
   
   # last_name 인원수
   SELECT LAST_NAME, COUNT(*) FROM USERS_USER GROUP BY LAST_NAME;
   ```
   



![image-20220418034915006](SQL_ORM.assets/image-20220418034915006.png)![image-20220418034955604](SQL_ORM.assets/image-20220418034955604.png)

![image-20220418035030373](SQL_ORM.assets/image-20220418035030373.png)

![image-20220418023934290](SQL_ORM.assets/image-20220418023934290.png)

![image-20220418024016445](SQL_ORM.assets/image-20220418024016445.png)

![image-20220418024024671](SQL_ORM.assets/image-20220418024024671.png)

![image-20220418024045284](SQL_ORM.assets/image-20220418024045284.png)

![image-20220418024238348](SQL_ORM.assets/image-20220418024238348.png)

![image-20220418032728842](SQL_ORM.assets/image-20220418032728842.png)

![image-20220418032734296](SQL_ORM.assets/image-20220418032734296.png)

![image-20220418033130912](SQL_ORM.assets/image-20220418033130912.png)

![image-20220418033135481](SQL_ORM.assets/image-20220418033135481.png)

![image-20220418033146432](SQL_ORM.assets/image-20220418033146432.png)

```
db01
```

![image-20220418033308425](SQL_ORM.assets/image-20220418033308425.png)





```
django2
```

![image-20220418034049051](SQL_ORM.assets/image-20220418034049051.png)

![image-20220418034054213](SQL_ORM.assets/image-20220418034054213.png)

![image-20220418034400102](SQL_ORM.assets/image-20220418034400102.png)

![image-20220418034411595](SQL_ORM.assets/image-20220418034411595.png)