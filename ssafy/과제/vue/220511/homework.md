#### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

```
- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다. F
- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다. F
- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다. F
- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다. T
```



#### 2. Vuex에서 State, Getters, Mutations, Actions의 역할을 각각 서술하시오.

```
state
* 중앙에서 관리하는 모든 상태 정보 (data)
* Mutations에 의해 변경됨

Mutations
* state를 변경하는 유일한 방법
* 반드시 동기적 로직이러야 함
* 첫번째 인자로 항상 state를 받고, Actions의 commit()에 의해 호출

Actions
* Mutations를 commit()으로 호출
* 비동기 로직 작성 가능
* 항상 context객체를 받기 때문에 모든 속성에 접근 할 수 있으나 state를 변경해서는 안됨
* 컴포넌트에서 dispatch()에 의해 호출

Getters
* store의 상태를 기반하는 계산 값
* 실제 상태를 변경하지 않음
* computed 속성과 유사
```

#### 3. 컴포넌트에 작성된 Todo App 관련 코드를 Vuex의 Store로 옮기고자 한다.  빈 칸 (a), (b), (c), (d)에 들어갈 코드를 작성하시오.

````
a = state
b = getters
c = actions
d = todo
````

