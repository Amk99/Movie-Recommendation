import streamlit as st
import pandas as pd
import requests

import pickle

def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(id,'af226236ddb3aa000baf0d2a4ab4c4f3'))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sim[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:7]
    
    recommended_movies = []
    rmp = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        rmp.append(fetch_poster(movie_id))
    return recommended_movies,rmp
    

movies_dict = pickle.load(open('movies.pkl','rb'))
sim = pickle.load(open('sim.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

st.title('Movie and Book Recommendations')

selected_movie = st.selectbox(
     'Tell us the movie that you liked',
     movies_list)

st.write('You selected:', selected_movie)

if st.button('Recommend'):
    names,poster = recommend(selected_movie)

    col1, col2, col3 ,col4,col5,col6= st.columns(6)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])

    with col4:
        st.text(names[3])
        st.image(poster[3])

    with col5:
        st.text(names[4])
        st.image(poster[4])

    with col6:
        st.text(names[5])
        st.image(poster[5])
