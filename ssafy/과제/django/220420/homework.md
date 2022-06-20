

#### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

```
URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. T
HTTP Method는 GET과 POST 두 종류 뿐이다. F
‘https://www.fifa.com/worldcup/teams/team/43822/create/’는
계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다. F
```



#### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오

**mdn의 http 검색**

```
200 OK
요청이 성공적으로 되었습니다. 성공의 의미는 HTTP 메소드에 따라 달라집니다.
GET: 리소스를 불러와서 메시지 바디에 전송되었습니다.
HEAD: 개체 해더가 메시지 바디에 있습니다.
PUT 또는 POST: 수행 결과에 대한 리소스가 메시지 바디에 전송되었습니다.
TRACE: 메시지 바디는 서버에서 수신한 요청 메시지를 포함하고 있습니다.

400 Bad Request
이 응답은 잘못된 문법으로 인하여 서버가 요청을 이해할 수 없음을 의미합니다.

401 Unauthorized
비록 HTTP 표준에서는 "미승인(unauthorized)"를 명확히 하고 있지만, 의미상 이 응답은 "비인증(unauthenticated)"을 의미합니다. 클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 합니다.

403 Forbidden
클라이언트는 콘텐츠에 접근할 권리를 가지고 있지 않습니다. 예를들어 그들은 미승인이어서 서버는 거절을 위한 적절한 응답을 보냅니다. 401과 다른 점은 서버가 클라이언트가 누구인지 알고 있습니다.

404 Not Found
서버는 요청받은 리소스를 찾을 수 없습니다. 브라우저에서는 알려지지 않은 URL을 의미합니다. 이것은 API에서 종점은 적절하지만 리소스 자체는 존재하지 않음을 의미할 수도 있습니다. 서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위하여 이 응답을 403 대신에 전송할 수도 있습니다. 이 응답 코드는 웹에서 반복적으로 발생하기 때문에 가장 유명할지도 모릅니다.

500 Internal Server Error
서버가 처리 방법을 모르는 상황이 발생했습니다. 서버는 아직 처리 방법을 알 수 없습니다.
```



#### 3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오

```python
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fieds = '__all__'
```



#### 4.Serializers의 의미를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오

```
Never use CRUD function names in URIs
URI 안에 CRUD 함수를 사용하지 마라
```



