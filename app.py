import streamlit as st
import pickle
import pandas as pd
import requests

# 🔑 Replace this with your actual OMDb API key
OMDB_API_KEY = 'a52614cd'

# 🔍 Fetch movie poster by title
def fetch_poster_by_name(movie_title):
    title = movie_title.strip()
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Debug (optional): print to console
    # print("Fetching:", title, "| Response:", data)

    if data.get("Response") == "True" and data.get("Poster") != "N/A":
        return data["Poster"]
    else:
        return "https://via.placeholder.com/500x750.png?text=No+Poster+Found"

# 🎯 Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        recommended_posters.append(fetch_poster_by_name(title))
    return recommended_movies, recommended_posters

# 🧠 Load model and run data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 🌐 Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Search for a movie to get similar recommendations:',
    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
