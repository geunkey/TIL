<template>

  <div class="container" style="margin-top:50px">
    
    <div id="nav" class="card m-4" style="border: 10px solid rgb(132, 194, 245); background-color: white; width: 80rem">

        <h2 class="mt-3">인기 영화</h2>
        <div class="row scroll-sect recent-movies">
          <div class="row-inner">
            <div class="tile"  v-for="movie in popular_movie_list" :key="movie.id" @click="detail(movie.id)">
              <div class="tile-media" >
                <img class="tapmovie" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
              </div>
              <div class="text-center">
                <h5 class="movie-title">{{ movie.title }}</h5>
              </div>
            </div>
          </div>
        </div>
      

      <h2>최신 영화</h2>
      <div class="row scroll-sect recent-movies">
        <div class="row-inner">
          <div class="tile"  v-for="movie in recent_movie_list" :key="movie.id"  @click="detail(movie.id)">
              <div class="tile-media">
                <img class="tapmovie" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
              </div>
              <div class="text-center">
                <h5 class="movie-title">{{ movie.title }}</h5>
              </div>
          </div>
        </div>
      </div>

      <h2 class="mt-3"> 추천 영화</h2>
      <div class="row scroll-sect recent-movies">
        <div class="row-inner">
          <div class="tile"  v-for="movie in recommend_movie_list" :key="movie.id" @click="detail(movie.id)">
            <div class="tile-media" >
              <img class="tapmovie" :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`">
            </div>
            <div class="text-center">
              <h5 class="movie-title">{{ movie.title }}</h5>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import VueJwtDecode from 'vue-jwt-decode'



export default {
  name: "Recommend",
  data: function() {
    return {
      user: '',
      popular_movie_list: [],
      recent_movie_list: [],
      recommend_movie_list: [],

    }
  },
  methods: {
    detail(movie_pk) {
      this.$router.push({
        name: 'MovieDetail',
        params: {movieId: movie_pk}
      })
    },
    getToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        },
      }
      return config
    },
    getMovieData: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post('http://127.0.0.1:8000/movies/recommend/',info, config)
      .then((res) => {
        console.log(res)
        this.popular_movie_list = res.data[0]
        this.recent_movie_list = res.data[1]
        this.recommend_movie_list = res.data[2]
      })
    },
    getUser: function () {
      const config = this.getToken()
      const hash = localStorage.getItem('jwt')
      const info = VueJwtDecode.decode(hash)
      axios.post('http://127.0.0.1:8000/accounts/profile/', info, config)
      .then((res) => {
        this.user = res.data
        // console.log(res)
        this.getMovieData()
      })
    },
  },
  created: function () {
    this.getMovieData()
  }
}
</script>


<style>
.movie-title{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 250px;
}
.row {
  overflow:scroll;
  width:92%;
}

.row-inner {
  white-space: nowrap;
  transition: 0.45s all;
  margin: 50px 10px;
}

.tile {
  position: relative;
  display:inline-block;
  margin: 0 5px;
  transition: 0.45s all;
  transform-origin: left center;
}

.tapmovie {
  width:250px;
  height:150px;
  object-fit:cover;
  
}

.recent-movies {
  margin-bottom: 30px;
}
.row-inner:hover
{
  /*move to the left */
  transform: translateX(calc(250px*(-0.5)/2));
}

.row-inner:hover .tile {
  
  opacity: .3;
  
}

.row-inner:hover .tile:hover {
  /*set opacity back to 1 */
  transform: scale(1.5);
  opacity: 1;
  
}

.tile:hover ~ .tile {
  /* move tiles on the right to the right*/
  transform: translateX(calc(250px * 0.5));
}

.scroll-sect{
  overflow: hidden;
  
}
.scroll-sect::-webkit-scrollbar {
  width: 8px; height: 8px; border: 3px solid white; 
  } 
.scroll-sect::-webkit-scrollbar-button,.scroll-sect::-webkit-scrollbar-button:END {
  background-color: white;
}
.scroll-sect::-webkit-scrollbar-button:start:decrement{
}

.scroll-sect::-webkit-scrollbar-track {
  background: white; 
  -webkit-border-radius: 10px white; 
  border-radius:10px white;
  /* -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,.2) */
  }

.scroll-sect::-webkit-scrollbar-thumb {
  height: 10px; 
  width: 50px; 
  background: #345389; 
  -webkit-border-radius: 15px; border-radius: 15px; 
  /* -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,.1) */
  }

.scroll-sect:hover{
  overflow-x: scroll;
}

[tooltip] {
  position: relative; /* opinion 1 */
}

/* START TOOLTIP STYLES */
[tooltip] {
  position: relative; /* opinion 1 */
}

/* Applies to all tooltips */
[tooltip]::before,
[tooltip]::after {
  text-transform: none; /* opinion 2 */
  font-size: .5em; /* opinion 3 */
  line-height: 1;
  user-select: none;
  pointer-events: none;
  position: absolute;
  display: none;
  opacity: 0;
}
[tooltip]::before {
  content: '';
  border: 5px solid transparent; /* opinion 4 */
  z-index: 1001; /* absurdity 1 */
}
[tooltip]::after {
  content: attr(tooltip); /* magic! */
  
  /* most of the rest of this is opinion */
  font-family:  'Noto Sans KR', Helvetica, sans-serif;
  text-align: center;
  
  /* 
    Let the content set the size of the tooltips 
    but this will also keep them from being obnoxious
    */
  min-width: 3em;
  max-width: 21em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding: 1ch 1.5ch;
  border-radius: .3ch;
  box-shadow: 0 1em 2em -.5em rgba(0, 0, 0, 0.35);
  background: #333;
  color: #fff;
  z-index: 1000; /* absurdity 2 */
}

/* Make the tooltips respond to hover */
[tooltip]:hover::before,
[tooltip]:hover::after {
  display: block;
}

/* don't show empty tooltips */
[tooltip='']::before,
[tooltip='']::after {
  display: none !important;
}



/* FLOW: RIGHT */
[tooltip][flow^="right"]::before {
  top: 50%;
  border-left-width: 0;
  border-right-color: #333;
  right: calc(0em - 5px);
  transform: translate(.5em, -50%);
}
[tooltip][flow^="right"]::after {
  top: 50%;
  left: calc(100% + 5px);
  transform: translate(.5em, -50%);
}

/* KEYFRAMES */
@keyframes tooltips-vert {
  to {
    opacity: .9;
    transform: translate(-50%, 0);
  }
}

@keyframes tooltips-horz {
  to {
    opacity: .9;
    transform: translate(0, -50%);
  }
}

/* FX All The Things */ 
[tooltip]:not([flow]):hover::before,
[tooltip]:not([flow]):hover::after,
[tooltip][flow^="up"]:hover::before,
[tooltip][flow^="up"]:hover::after,
[tooltip][flow^="down"]:hover::before,
[tooltip][flow^="down"]:hover::after {
  animation: tooltips-vert 300ms ease-out forwards;
}

[tooltip][flow^="left"]:hover::before,
[tooltip][flow^="left"]:hover::after,
[tooltip][flow^="right"]:hover::before,
[tooltip][flow^="right"]:hover::after {
  animation: tooltips-horz 300ms ease-out forwards;
}


main {
  flex: 1 1 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

main div {
  text-align: center;
  color: #353539;
}
main span {
  padding: .5em 1em;
  margin: .5em;
  display: inline-block;
  background: #dedede;
}

.text-center {
  font-family: 'Do Hyeon', sans-serif;
}

h2 {
  font-family: 'Gugi';
}
th, td {
  font-family: 'Noto Sans KR';
  background-color: white;
}

table{
  border-style: none;
}

.table thead th {
  border-top-style: none;
}
/* 
@media (max-width: 576px){
  .show-small {
    width: 90%;
  }
} */
</style>
