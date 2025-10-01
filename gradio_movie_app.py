import gradio as gr
import pickle
import pandas as pd
import requests

# Load Movies and Similarity
movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

OMDB_API_KEY = "c6488acc"


def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url).json()
    if response.get("Poster") and response["Poster"] != "N/A":
        return response["Poster"]
    return "https://via.placeholder.com/200x300?text=No+Poster"


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

    # List of (image, label) tuples for Gradio Gallery
    output = [(poster, title) for poster, title in zip(recommended_posters, recommended_movies)]
    return output


# Gradio Interface
iface = gr.Interface(
    fn=recommend,
    inputs=gr.Dropdown(choices=movies['title'].tolist(), label="Select a movie"),
    outputs=gr.Gallery(label="Recommended Movies", columns=5, show_label=True, elem_id="movie-gallery"),
    title="🎬 Movie Recommender System with OMDb Posters"
)

iface.launch()
