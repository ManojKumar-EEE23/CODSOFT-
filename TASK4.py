import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample movie dataset
data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['Inception', 'The Dark Knight', 'Interstellar', 'The Matrix', 'Shutter Island'],
    'Genre': ['Sci-Fi', 'Action', 'Sci-Fi', 'Sci-Fi', 'Thriller']
}

movies_df = pd.DataFrame(data)

# User ratings
ratings_data = {
    'UserID': [101, 101, 102, 103, 104],
    'MovieID': [1, 2, 3, 4, 5],
    'Rating': [5, 4, 5, 3, 4]
}

ratings_df = pd.DataFrame(ratings_data)

# Content-Based Filtering
def content_based_recommendations(movie_title, movies_df):
    tfidf = TfidfVectorizer(stop_words='english')
    movies_df['Genre'] = movies_df['Genre'].fillna('')
    tfidf_matrix = tfidf.fit_transform(movies_df['Genre'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(movies_df.index, index=movies_df['Title']).drop_duplicates()
    
    if movie_title not in indices:
        return f"Movie '{movie_title}' not found. Please try again."
    
    idx = indices[movie_title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['Title'].iloc[movie_indices]

# Collaborative Filtering (User-Item Matrix)
def collaborative_filtering(user_id, ratings_df):
    user_movie_matrix = ratings_df.pivot(index='UserID', columns='MovieID', values='Rating').fillna(0)
    user_sim = cosine_similarity(user_movie_matrix)
    user_sim_df = pd.DataFrame(user_sim, index=user_movie_matrix.index, columns=user_movie_matrix.index)
    
    if user_id not in user_sim_df.index:
        return f"User ID '{user_id}' not found. Please try again."

    similar_users = user_sim_df[user_id].sort_values(ascending=False).index[1]
    recommended_movie_id = user_movie_matrix.loc[similar_users].idxmax()
    
    movie_title = movies_df.loc[movies_df['MovieID'] == recommended_movie_id].Title.values[0]
    return movie_title

# Get User Input for Content-Based Filtering
user_movie = input("Enter a movie title for recommendations: ")
print("\nContent-Based Recommendations:")
print(content_based_recommendations(user_movie, movies_df))

# Get User Input for Collaborative Filtering
try:
    user_id = int(input("\nEnter a user ID for collaborative filtering recommendation: "))
    print("\nCollaborative Filtering Recommendation:")
    print(collaborative_filtering(user_id, ratings_df))
except ValueError:
    print("Invalid input. Please enter a numeric User ID.")
