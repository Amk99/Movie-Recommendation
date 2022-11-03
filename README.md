# Movie-Recommendation

### Deciding which movie to pick is a tedious job!!

#### This simple movie REcommendation system suggests movies that are similar to the oones that yo like.

This recommendation model is trained on TMDB movies dataset.It suggests similar movies based on similaritie in the movie description, actorss in the movie and director.(in that order)
A bag of words model is used to tokenize the information which is then used to find similar movies using cosine distance formula.TMDB API is then called to fetch the movie poster.
Hosted on netlify.

Check out the live demo here:
