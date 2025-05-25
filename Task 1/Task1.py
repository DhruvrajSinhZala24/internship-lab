# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('Dataset.csv')

# Clean and preprocess data

# Drop unnecessary columns
df = df.drop([
    'Restaurant ID', 'Restaurant Name', 'Address', 'Locality Verbose',
    'Longitude', 'Latitude', 'Currency', 'Votes', 'Rating text'
], axis=1, errors='ignore')

# Only keep rows where 'Aggregate rating' is numeric
df = df[df['Aggregate rating'].astype(str).str.replace('.', '', regex=False).str.isnumeric()]
df['Aggregate rating'] = df['Aggregate rating'].astype(float)

# Fill missing values in other categorical features
df['Cuisines'] = df['Cuisines'].fillna("Unknown")

# Define categorical columns
categorical_cols = [
    'Country Code', 'City', 'Locality', 'Cuisines',
    'Has Table booking', 'Has Online delivery',
    'Is delivering now', 'Switch to order menu',
    'Rating color', 'Price range'
]

# One-hot encode categorical variables
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# Define features and target
X = df_encoded.drop('Aggregate rating', axis=1)
y = df_encoded['Aggregate rating']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.4f}")
print(f"R-squared: {r2:.4f}")

# Show feature importance
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', key=abs, ascending=False)

print("\nTop Influential Features:")
print(feature_importance.head(10))