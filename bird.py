# Import necessary libraries
import os
import numpy as np
import librosa
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load
from tkinter import Tk, Button, Label, filedialog

# Function to extract audio features (Mel-frequency cepstral coefficients - MFCCs)
def extract_features(file_path, num_mfcc=13, n_fft=2048, hop_length=512):
    audio, _ = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(audio, sr=None, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
    return np.mean(mfccs.T, axis=0)

# Function to train the model
def train_model(data_dir):
    features = []
    labels = []

    # Load labeled audio data
    for bird_species in os.listdir(data_dir):
        species_path = os.path.join(data_dir, bird_species)
        if os.path.isdir(species_path):
            for filename in os.listdir(species_path):
                file_path = os.path.join(species_path, filename)
                if filename.endswith('.wav'):
                    features.append(extract_features(file_path))
                    labels.append(bird_species)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Train a machine learning model (Random Forest Classifier in this example)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

    # Save the trained model
    dump(model, 'bird_species_model.joblib')

# Function to predict bird species from an audio file
def predict_species(file_path):
    # Load the trained model
    model = load('bird_species_model.joblib')

    # Extract features from the input audio file
    features = extract_features(file_path)

    # Make predictions
    prediction = model.predict([features])
    return prediction[0]

# Function to handle file selection and prediction
def choose_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
    if file_path:
        predicted_species = predict_species(file_path)
        result_label.config(text=f"Predicted Bird Species: {predicted_species}")

# GUI setup
root = Tk()
root.title("Bird Species Identification App")

choose_file_button = Button(root, text="Choose Audio File", command=choose_file)
choose_file_button.pack(pady=20)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()

