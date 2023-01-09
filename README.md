# Movie-Recommendation

### Deciding which movie to pick is a tedious job!!

#### This simple movie Recommendation system suggests movies that are similar to the ones that yo like.

This recommendation model is trained on TMDB movies dataset.It suggests similar movies based on similaritie in the movie description, actorss in the movie and director.(in that order)
A bag of words model is used to tokenize the information which is then used to find similar movies using cosine distance formula.TMDB API is then called to fetch the movie poster.Model is converted to web app using streamlit
Hosted on Heroku free tier (takes time to load)

[Check out Live Demo here](https://amk99-movie-recommendation-app-6x3y8q.streamlit.app/)
### ScreenShots:

<img src="https://github.com/Amk99/Movie-Recommendation/blob/main/movie_rec/images/Screenshot%20(22).png?raw=true" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="600" height="400" />

<br>
<img src="https://github.com/Amk99/Movie-Recommendation/blob/main/movie_rec/images/Screenshot%20(23).png?raw=true" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="600" height="400" />
