import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load data
movies = pd.read_csv("movies.csv")
tags = pd.read_csv("tags.csv")

# Clean and prepare
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)
tags['tag'] = tags['tag'].fillna('').astype(str)
tags_grouped = tags.groupby('movieId')['tag'].apply(lambda x: ' '.join(x)).reset_index()
movies = pd.merge(movies, tags_grouped, on='movieId', how='left')
movies['tag'] = movies['tag'].fillna('')
movies['content'] = movies['genres'] + ' ' + movies['tag']

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['content'])

# NearestNeighbors
nn = NearestNeighbors(metric='cosine', algorithm='brute')
nn.fit(tfidf_matrix)

# Reverse index
title_to_index = pd.Series(movies.index, index=movies['title']).drop_duplicates()

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get similar recommendations:")

selected_movie = st.selectbox("Choose a movie", movies['title'].sort_values())

if st.button("Recommend"):
    idx = title_to_index[selected_movie]
    distances, indices_recommended = nn.kneighbors(tfidf_matrix[idx], n_neighbors=6)

    st.subheader("🎯 Because you liked: " + selected_movie)
    st.write("👉 You might also like:")
    for i, rec_idx in enumerate(indices_recommended[0][1:], 1):
        st.write(f"{i}. {movies['title'].iloc[rec_idx]}")
