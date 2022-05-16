#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```
 - Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다. T

- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.
 XHR객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다. F

- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.T 
```





#### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

![image-20220503124910814](homework.assets/image-20220503124910814.png)

```
먼저 Call Stack에 'Hello SSAFY!'가 입력되면서 출력되고,
그 다음 Call Stack에 'I am from setTimeout'이 입력되면서 Web API로 가서 1초간 대기한다.
그 사이 Call Stack에 'Bye SSAFY!'가 입력되면서 출력된다.
그 다음 'I am from setTimeout'은 Task Queue로 이동한 후 다시 Call Stack으로 이동 후 출력된다.
```

