import streamlit as st
import pickle
import pandas as pd
import requests

# ===============================
# Load Movies and Similarity
# ===============================
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

OMDB_API_KEY = "c6488acc"

# ===============================
# Function to fetch poster from OMDb
# ===============================
def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    if response.get("Poster") and response["Poster"] != "N/A":
        return response["Poster"]
    return None

# ===============================
# Function to recommend movies
# ===============================
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster(title))
    return recommended_movies, recommended_posters

# ===============================
# Streamlit App
# ===============================
st.title("🎬 Movie Recommender System with OMDb Posters")

selected_movie_name = st.selectbox("Select a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(len(names))  # Create a column for each recommended movie
    placeholder = "https://via.placeholder.com/200x300?text=No+Poster"

    for col, name, poster in zip(cols, names, posters):
        col.image(poster if poster else placeholder, width=150)
        col.write(name)
