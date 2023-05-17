import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('cervical_cancer_dataset.csv')

# Preprocess the data
df.dropna(inplace=True)
X = df.drop('Cervical cancer diagnosis', axis=1)
y = df['Cervical cancer diagnosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Define the Streamlit app
def cervical_cancer_diagnosis():
    st.title("Cervical Cancer Diagnosis")
    st.write("Answer a few questions to determine if cervical cancer is likely.")

    age = st.slider("Age", 18, 100)
    sexual_partners = st.slider("Number of Sexual Partners", 0, 20)
    # Add more questions for other features in the dataset

    if st.button("Diagnose"):
        # Create a new dataframe with the user's input
        user_input = pd.DataFrame({
            'Age': [age],
            'Number of sexual partners': [sexual_partners],
            # Add more columns for other features in the dataset
        })

        # Make predictions using the trained model
        prediction = model.predict(user_input)
        probability = model.predict_proba(user_input)

        # Display the diagnosis result
        st.subheader("Diagnosis Result")
        if prediction[0] == 0:
            st.write("No Cervical Cancer detected.")
        else:
            st.write("Cervical Cancer detected.")
        st.write("Probability: {:.2f}%".format(probability[0][1] * 100))

# Run the Streamlit app
if __name__ == '__main__':
    cervical_cancer_diagnosis()
