# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

# Load dataset
df = pd.read_csv('Dataset.csv')

# Clean and preprocess
df['Cuisines'] = df['Cuisines'].fillna("Unknown").str.split(",").str[0].str.strip()
df['Price range'] = df['Price range'].astype(str).fillna("0")

# Select features
features = ['Aggregate rating', 'Price range', 'City', 'Has Online delivery', 'Has Table booking']
X = df[features]

# Encode features
X = pd.get_dummies(X, drop_first=True)

# Encode target
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['Cuisines'])

# Filter out rare cuisines
class_counts = pd.Series(y).value_counts()
valid_classes = class_counts[class_counts >= 5].index
mask = np.isin(y, valid_classes)

X_filtered = X[mask]
y_filtered = y[mask]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_filtered, y_filtered, test_size=0.2, random_state=42, stratify=y_filtered
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Print report
valid_cuisine_names = label_encoder.classes_[valid_classes]
print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=valid_cuisine_names,
    labels=valid_classes,
    zero_division=0
))