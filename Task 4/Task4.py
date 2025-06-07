# Import required libraries
import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser
import os

# Load and clean data
df = pd.read_csv('Dataset.csv')

# Drop rows with missing latitude/longitude
df = df.dropna(subset=['Latitude', 'Longitude'])

# Fill missing values
df['Cuisines'] = df['Cuisines'].fillna("Unknown").str.split(",").str[0].str.strip()
df['City'] = df['City'].fillna("Unknown")
df['Price range'] = pd.to_numeric(df['Price range'], errors='coerce').fillna(0)
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce').fillna(0)

# Create interactive map using Folium
# Initialize map around India
restaurant_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add restaurant markers
for _, row in df.iterrows():
    if row['Latitude'] != 0 and row['Longitude'] != 0:  # Skip invalid coordinates
        popup_text = f"""
        <strong>{row['Restaurant Name']}</strong><br>
        City: {row['City']}<br>
        Cuisine: {row['Cuisines']}<br>
        Rating: {row['Aggregate rating']} ({row['Rating text']})<br>
        Price Range: {row['Price range']}
        """
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,
            color='crimson',
            fill=True,
            fill_color='crimson',
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(restaurant_map)

# Save map to HTML file
restaurant_map.save('restaurant_map.html')
webbrowser.open('file://' + os.path.realpath("restaurant_map.html"))
print("✅ Interactive map saved as 'restaurant_map.html'")

# Top Cuisines Bar Chart
plt.figure(figsize=(12, 6))
top_cuisines = df['Cuisines'].value_counts().head(10)
sns.barplot(x=top_cuisines.values, y=top_cuisines.index, palette="viridis")
plt.title("Top 10 Cuisines")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()

# Average Ratings by City
city_ratings = df.groupby('City')['Aggregate rating'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=city_ratings.values, y=city_ratings.index, palette="coolwarm")
plt.title("Top Cities by Average Restaurant Rating")
plt.xlabel("Average Rating")
plt.ylabel("City")
plt.tight_layout()
plt.show()