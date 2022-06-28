1. ```text
   hw_ws/web_220203/ssafy 를 봐주세요. 
   ```
   
   ![workshop1_1](https://lab.ssafy.com/rlawowns97/hw_ws/-/raw/master/web_220203/IMAGE/workshop1_1.png)
   
   로컬 절대경로로 했을 때 잘 나오는 것 확인.
   
   <br>
   
   ![workshop1_2](https://lab.ssafy.com/rlawowns97/hw_ws/-/raw/master/web_220203/IMAGE/workshop1_2.png)
   
   잘못된 경로가 입력되었을 때 `ssafy` 라는 글자가 출력되게 한 것 확인.
   
   <br>
   
   
   
2. ```text
   (a) : 절대 경로
   (b) : 상대 경로
   ```
   ```html
   <!-- (b)로 작성한 HTML -->
   <!DOCTYPE html>
   <html lang="en">
   
     <head>
       <meta charset="utf-8">
       <title></title>
     </head>
   
     <body>
       <!-- 절대경로로 했을 때 코드 -->
       <!-- <img src="/Users/xi-jjun/workspace/ssafy/gitlab/hw_ws/web_220203/ssafy/image/my_photo.png" alt="ssafy"> -->
       
       <!-- 상대경로로 변경한 후 경로 -->
       <img src="../image/my_photo.png" alt="ssafy">
     </body>
   
   </html>
   ```
   
   
   
3. ```text
   hw_ws/web_220203/ssafy 를 봐주세요.
   ```
   
4. 
   
   - 4-(1) 결과
   
   ![workshop4_1](./IMAGE/workshop4_1.png)
   
   - 4-(2) 결과
   
   ![workshop4_2](./IMAGE/workshop4_2.png)
   
   - `nth-child` vs `nth-of-type`
   
     - `nth-child(n)` : 부모 element의 모든 자식 element 중에 n번째
   
       ```html
       ... (생략)
           <style>
             /* 4-(1) */
             #ssafy>p:nth-child(2) {
               color: red;
             } 
           </style>
       ... (생략)
       
         <body>
           <div id="ssafy"> <!-- 부모 element! -->
             <h2>어떻게 선택 될까?</h2> <!-- nth-child(1) -->
             <p>1번째 단락</p> <!-- nth-child(2) -->
             <p>2번째 단락</p> <!-- nth-child(3)... -->
             <p>3번째 단락</p>
             <p>4번째 단락</p>
           </div>
         </body>
       ```
   
       
   
     - `nth-of-type(n)` : 부모 element의 특정 자식 element 중 n번째 → 특정 element 중에서의 순서를 고른다.
   
       ```html
       ... (생략)
           <style>
             /* 4-(2) */
             #ssafy>p:nth-of-type(2) {
               color: red;
             }
           </style>
       ... (생략)
       
         <body>
           <div id="ssafy"> <!-- 부모 element! -->
             <h2>어떻게 선택 될까?</h2>
             <p>1번째 단락</p> <!-- p:nth-of-type(1) p tag 만 순서를 센다!!-->
             <p>2번째 단락</p> <!-- p:nth-of-type(2) -->
             <p>3번째 단락</p> <!-- p:nth-of-type(3) -->
             <p>4번째 단락</p> <!-- p:nth-of-type(4) -->
           </div>
         </body>
       ```
   
       
   
   
   
   