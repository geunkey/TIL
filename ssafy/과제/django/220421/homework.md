#### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

```
- JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다. 
	: 내장 HttpResponse를 활용해도 된다. F
 
- DRF가 제공하는 기본 Form을 통해서만 여러 HTTP Method를 테스트 해볼 수 있다.
	: JsonResponse객체를 활용해도 된다. F
	
- api_view 데코데이터를 사용하지 않아도 HTTP Method에 대한 요청에 응답할 수 있다.
	: DRF에서는 필수적으로 작성해야 해당 view 함수가 정상적으로 동작한다. F

- Serializers는 Queryset 객체를 JSON 포맷으로 변환 할 수 있는 python 데이터 타입으로 만들어준다.
	 : T
```



#### 2. REST API 디자인 가이드

```
a = URI
b = HTTP Method
```



#### 3.아래에서 빈칸 a, b, c, d, e 에 들어갈 코드를 작성하시오.

````
a = ['POST']
b = data=request.data
c = raise_exception=True
d = serializer.data
e = status=status.HTTP_201_CREATED
````

