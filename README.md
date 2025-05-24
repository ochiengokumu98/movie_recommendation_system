
# 🎬 Movie Recommendation System

A content-based movie recommender system built using Python, Scikit-learn, and Streamlit.
The system suggests movies similar to a selected title based on genres and user tags.

---

## 📌 Features

- 🔍 Searchable movie dropdown
- 🤖 TF-IDF-based content similarity
- 💡 Instant recommendations
- 🎨 Clean Streamlit user interface
- 📁 Built using open MovieLens datasets

---

## 📂 Datasets Used

From [MovieLens](https://grouplens.org/datasets/movielens/), the following CSV files are used:

- `movies.csv`: Movie ID, title, genres
- `ratings.csv`: (Optional, not used in current version)
- `tags.csv`: User-assigned tags  (too large to be uploaded ) please download from the link above.
- `links.csv`: (Optional, for future use with posters or APIs)

### 2. Install dependencies

```bash
pip install -r requirements.txt
```
Or manually install key packages:
```bash
pip install pandas scikit-learn streamlit
```
### 3. Run the app
If you're using a terminal:
```bash
streamlit run app.py
```
If you're in Jupyter Notebook:

```python
!streamlit run app.py

---

## 🧠 How It Works

1. **TF-IDF Vectorization**: Converts genres + tags into a vector space.
2. **Cosine Similarity**: Finds movies with the most similar vectors.
3. **Nearest Neighbors**: Retrieves top 5 recommendations based on similarity.

---

## 🎯 To-Do / Future Enhancements

* 🎞️ Add movie posters using TMDb or OMDb API
* ⭐ Integrate ratings and popularity
* 🧠 Switch to hybrid (content + collaborative) filtering
* 💾 Allow users to rate and save favorites

---

## 🛠 Built With

* [Python](https://www.python.org/)
* [Scikit-learn](https://scikit-learn.org/)
* [Streamlit](https://streamlit.io/)
* [MovieLens Dataset](https://grouplens.org/datasets/movielens/)

---

## 👨‍💻 Author

**Ochieng Okumu**
Data Analyst | Machine Learning Enthusiast
📧 Reach me on [LinkedIn](www.linkedin.com/in/ochiengokumu2030)


## ✅ Optional: Create `requirements.txt`

```txt
pandas
scikit-learn
streamlit
````

Thank you.
