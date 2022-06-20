# 1. 한국어로 번역하기

1)LANGUAGE_CODE = 'ko-kr'

2)USE_I18N = True



 # 2. 경로 설정하기

path('ssafy/', views.ssafy),



# 3. Django Template Language

1. menu

2. forloop.counter0

3. empty

4. a = if         b = else
5. a = length       b = title 또는 capfirst
6. Y년 m월 d일 (D) h:i



#  4. Form tag with Django

1) 입력된 데이터가 전송될 URL를 지정한다
2) 데이터를 보내는데 사용되는 HTTP 메소드로 post, get을 가진다.
   get : 보안상 취약, 길이 제한
   post : 보안 강함, 길이 무제한
3) /create/?title=안녕하세요&content=반갑습니다&my-site=파이팅