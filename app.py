import os
import pickle

import streamlit as st
import  joblib

st.title("Movie Recommendation System")
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the full path to movies.pkl
movies_path = os.path.join(current_dir, "movies.pkl")
# Open the file
with open(movies_path, "rb") as m:
    movies = pickle.load(m)

similarity_path = os.path.join(current_dir, "similarities.joblib")

with open(similarity_path, "rb") as s:
    similarities = joblib.load(s)

recommended_movies = []

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name.lower()].index[0]
    recommendations = similarities[movie_index]
    movies_list = sorted(enumerate(recommendations),reverse=True,key=lambda x:x[1])[1:6]
    for item in movies_list:
        recommended_movies.append(movies.iloc[item[0]].title.title())
    return recommended_movies

movies_names = movies['title'].apply(lambda x:x.title()).values
selected_movie = st.selectbox("Select the movie title", movies_names)
if st.button("Recommend Movie"):
    recommended_list = recommend(selected_movie)
    st.write(f"Recommended Movies are:")
    for m in recommended_list:
        st.write(f"{m}")