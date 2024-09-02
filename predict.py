import os
import pickle
import tensorflow as tf
from keras.models import load_model

# Define the combinations
combinations = ['E0-I1', 'N0-S1', 'F0-T1', 'J0-P1']

# Load the saved models
l_models = {combination: load_model(f'model/{combination}.h5') for combination in combinations}

# Load the saved vectorizer
with open('model/vectorizer.pkl', 'rb') as f:
    l_vectorizer = pickle.load(f)

# Simulate new data (replace this with your actual new data)
new_post = "this is a new post another post for testing yet another post"

# Preprocess new data using the loaded vectorizer
X_new = l_vectorizer.transform([new_post]).toarray()

# Make predictions for each combination
y_preds = []
for combination, model in l_models.items():
    y_pred = model.predict(X_new)
    if y_pred >= 0.5:
        if combination == 'E0-I1':
            y_preds.append('I')
        elif combination == 'N0-S1':
            y_preds.append('S')
        elif combination == 'F0-T1':
            y_preds.append('T')
        else:
            y_preds.append('P')
    else:
        if combination == 'E0-I1':
            y_preds.append('E')
        elif combination == 'N0-S1':
            y_preds.append('N')
        elif combination == 'F0-T1':
            y_preds.append('F')
        else:
            y_preds.append('J')

# Concatenate the predictions for each combination into a single string
prediction = ''.join(y_preds)

# Print the concatenated prediction
print(f"Prediction: {prediction}")