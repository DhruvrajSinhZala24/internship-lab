# Import required libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv('Dataset.csv')

# Feature selection & preprocessing

# Fill missing values
df['Cuisines'] = df['Cuisines'].fillna("Unknown")
df['Price range'] = df['Price range'].astype(str).fillna("0")

# Combine relevant features into a single string
df['Features'] = (
    df['Cuisines'] + " " +
    df['Price range'].astype(str) + " " +
    df['City'] + " " +
    df['Locality']
)

# Vectorize using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend similar restaurants
def recommend_similar_restaurants(restaurant_name_or_id, num_recommendations=5):
    # Find matching row(s)
    if str(restaurant_name_or_id).isdigit():
        matches = df[df['Restaurant ID'] == int(restaurant_name_or_id)]
    else:
        matches = df[df['Restaurant Name'].str.contains(restaurant_name_or_id, case=False, na=False)]

    if matches.empty:
        return f"No restaurant found matching '{restaurant_name_or_id}'"

    idx = matches.index[0]  # Get first match index
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  # Skip self
    restaurant_indices = [i[0] for i in sim_scores]

    recommendations = df.iloc[restaurant_indices][[
        'Restaurant Name', 'Cuisines', 'Price range', 'Aggregate rating', 'City', 'Locality'
    ]]
    
    return recommendations

# Test with sample restaurant
sample_input = "Shahenshah"  # Can also use an ID like 18255715

print(f"\nTop 5 Restaurants Similar to '{sample_input}':\n")
result = recommend_similar_restaurants(sample_input)
print(result.to_string(index=False))