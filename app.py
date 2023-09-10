import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    ind = movies[movies['title'] == movie].index[0]
    distances = simi[ind]
    m = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    remo = []
    remo_posters=[]
    for i in m:
        movie_id = movies.iloc[i[0]].movie_id
        remo_posters.append(fetch_poster(movie_id))
        remo.append(movies.iloc[i[0]]['title'])  # Change movies_list.iloc[i[0]].title to movies_list[i[0]]['title']
    return remo,remo_posters

# Load the data
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_list)

# Function to recommend movies

st.title('Movie Recommender System')
simi = pickle.load(open('simi_2.pkl', 'rb'))
selected_movie_name = st.selectbox(
    'Select a movie:', movies['title'].values)

if st.button('Recommend'):



    col1, col2, col3 = st.columns(3)
    names ,posters= recommend(selected_movie_name)
    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])
    with col3:
        st.header(names[3])
        st.image(posters[3])
