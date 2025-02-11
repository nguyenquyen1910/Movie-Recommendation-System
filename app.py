import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f0b17c4702cb9eea0a602923f494f0e8&language=en-US".format(
        movie_id
    )
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


def recommend(movie):
    index_of_the_movie = movies[movies["title"] == movie]["index"].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    recommended_movies_name = []
    recommended_movies_poster = []
    for movie_item in sorted_similar_movies[1:6]:
        movie_id = movies.iloc[movie_item[0]]["id"]
        recommended_movies_name.append(movies.iloc[movie_item[0]]["title"])
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name, recommended_movies_poster


st.header("Movie Recommendation System Using Machine Learning")
movies = pickle.load(open("artificats/movie_list.pkl", "rb"))
similarity = pickle.load(open("artificats/similary.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie to get recommendation", movie_list
)


if st.button("Show recommendations"):
    recommended_movies_name, recommeded_movies_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recommended_movies_name[0])
        st.image(recommeded_movies_poster[0])

    with col2:
        st.write(recommended_movies_name[1])
        st.image(recommeded_movies_poster[1])

    with col3:
        st.write(recommended_movies_name[2])
        st.image(recommeded_movies_poster[2])

    with col4:
        st.write(recommended_movies_name[3])
        st.image(recommeded_movies_poster[3])

    with col5:
        st.write(recommended_movies_name[4])
        st.image(recommeded_movies_poster[4])
