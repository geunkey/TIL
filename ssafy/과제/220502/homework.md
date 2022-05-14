#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오

```
- JavaScript는 single threaded 언어로 한 번에 한 가지 일 밖에 처리하지 못한다.
 : True

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다.
: False (setTimeout 작업이 stack에 등록되고, Web API에 setTimeout을 요청하고 Callback 함수를 전달한다. 요청한 후 Call Stack에서 setTimeout이 제거된다.
)
```



#### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

```python
동기(Synchronous)
동기는 요청을 보낸 후 응답(결과물)을 받아야지만 다음 동작이 이루어지는 방식을 말한다.
모든 일은 순차적으로 실행되며 어떤 작업이 수행중이라면 다음 작업은 대기하게 된다.

function func1() {
    console.log('첫번째 펑션!');
    func2();
}

function func2(){
    console.log('두번째 펑션!');
    func3();
}

function func3() {
    console.log('세번째 펑션');
}

func1();
// 출력값은 아래와 같다.
// 첫번째 펑션!
// 두번째 펑션!
// 세번째 펑션! 을 띄우게 된다.
```

```python
비동기(Asynchronous)
비동기 처리는 왜 필요한가? - 데이터를 서버로부터 받아오는 앱을 만든다고 가정하면,
서버로부터 데이터를 받아와서 해당 데이터를 뿌려줘야 하므로 맨 처음에 서버로부터 데이터를 받아오는 코드가 실행되어야 할 것이다.


비동기로 처리하지 않고 동기적으로 구성을 하게 된다면 데이터를 받아오기까지 기다린 다음에 앱이 실행될 것이고 서버에 가져오는 데이터 양이 늘어날수록 앱의 실행속도는 기하급수적으로 느려진다.


데이터를 가져오기까지 앱이 대기하는 상태가 발생하게 된다. 이런 불편을 없애기 위해서
데이터를 수신하는 코드와 페이지를 표시하는 것과는 비동기적으로 처리를 해야한다.
그래서 비동기처리로 가장 많이 드는 예가바로 setTimeout과 AJAX가 있다.

function func1(){
    console.log('func1');
    func2();
}

function func2(){
    setTimeout(function(){
        console.log('func2');
    }, 0);
    func3();
}

function func3(){
    console.log('func3');
}
func1();
/*
실행결과
func1
func3
func2
*/
```



#### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 정상적으로 응답이 왔을 때 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```
a = get
b = then
c = response.data
```