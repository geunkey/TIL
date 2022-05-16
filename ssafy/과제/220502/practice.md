#  팔로우 기능

![image-20220503171511851](practice.assets/image-20220503171511851.png)



## views.py

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        me = request.user
        you = get_object_or_404(get_user_model(), pk=user_pk)

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
            # if me in you.followers.all():
                # 언팔로우
                you.followers.remove(me)
                isFollowed = False
            else:
                # 팔로우
                you.followers.add(me)
                isFollowed = True
            context={
                'isFollowed': isFollowed,
                'followingCnt': you.followings.count(),
                'followersCnt' : you.followers.count(),
            }
            return JsonResponse(context)

            
        return redirect('accounts:profile', you.username)

    return redirect('accounts:login')
```



## profile.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}의 프로필 페이지</h1>
  {% with followings=person.followings.all followers=person.followers.all %}
    <div>
      <div id="follow-cnt">팔로잉 수 : {{ followings|length }} / 팔로워 수 : {{ followers|length }}</div>
    </div>
    {% if user != person %}
      <div>
        <form id="follow-form" data-person-id="{{ person.pk }}">
          {% csrf_token %}
          {% if user in followers %}
            <input type="submit" value="언팔로우">
          {% else %}
            <input type="submit" value="팔로우">
          {% endif %}
        </form>
      </div>
    {% endif %}
  {% endwith %}

  <hr>

  <h2>{{ person.username }}가 작성한 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}가 작성한 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}

  <hr>

  <h2>{{ person.username }}가 좋아요를 누른 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">[back]</a>
  
{% endblock content %}

{% block script %}
<script>
  // CODE HERE
  const followForm = document.querySelector('#follow-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  // console.log(followForm)
  if (followForm) {
    followForm.addEventListener('submit', (event)=>{
      event.preventDefault()
      const personId = event.target.dataset.personId
      //console.log(personId)
      // console.log(event)
  
      axios.post(`http://127.0.0.1:8000/accounts/${personId}/follow/`, {}, {headers: {'X-CSRFToken': csrftoken}})
        .then((response)=>{
          const { isFollowed, followingCnt, followersCnt } = response.data
          console.log(isFollowed, followingCnt, followersCnt)
  
          const cntDiv = document.querySelector('#follow-cnt')
          cntDiv.innerText = `팔로잉 수 : ${followingCnt} / 팔로워 수 : ${followersCnt}`
          const submitInput = document.querySelector('#follow-form > input[type=submit]')
          
          if (followersCnt) {
            submitInput.value = '언팔로우'
          }
          else {
            submitInput.value = '팔로우'
          }
  
        })
      //axios({
        //method: 'post',
        //url: 'http://127.0.0.1:8000/accounts/',
     // })
    })
  
  }
  


</script>
{% endblock script %}
```

