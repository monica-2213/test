import pandas as pd
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer_csv.csv'
data = pd.read_csv(url)

# Preprocess the data
data = data[['Age', 'Smokes', 'Biopsy']]
data['Smokes'] = data['Smokes'].map({'0': 0, '1': 1, '2': 1})
data = data.dropna()

# Train a decision tree model
X = data[['Age', 'Smokes']]
y = data['Biopsy']
model = DecisionTreeClassifier()
model.fit(X, y)

# Define the Streamlit app
st.title('Cervical Cancer Diagnosis Expert System')

# Ask for user input
age = st.slider('Age', 15, 84)
smokes = st.selectbox('Do you smoke?', ('No', 'Yes'))

# Preprocess the user input
smokes = 1 if smokes == 'Yes' else 0

# Make a prediction
prediction = model.predict([[age, smokes]])

# Display the prediction
if prediction[0] == 0:
    st.write('You do not have cervical cancer.')
else:
    st.write('You have cervical cancer.')
