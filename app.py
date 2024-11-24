import streamlit as st  # user inferface
import joblib           # load in our model
import pandas as pd     # data frame stuff :)

# Load the saved model
model = joblib.load('model.pkl')

# Define the function to make predictions
def predict(student_data):
    # Ensure the input is transformed into a DataFrame
    columns = [
        'Age', 'sex_male', 'sex_female', 'ParentalEducation', 'StudyTimeWeekly',
       'Absences', 'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports',
       'Music', 'Volunteering'
    ]
    student_df = pd.DataFrame([student_data], columns=columns)
    
    # Make prediction using the trained model
    prediction = model.predict(student_df)
    return prediction[0]

# Streamlit Interface

# Title and description
st.title("Student Performance Prediction")
st.write("""
    Enter the student details below to predict their performance.
    The prediction will be based on factors like GPA, study time, parental support, and more.
""")

# Input fields for the user to fill
Age = st.number_input("Age", min_value=15, max_value=100, value=18)
Gender = st.selectbox("Gender", options=["Male", "Female"], index=0)
Absences = st.number_input("Absences", min_value=0, max_value=30, value=0)
StudyTimeWeekly = st.number_input("Study Time Weekly (hours)", min_value=0, max_value=20, value=10)
ParentalSupport = st.selectbox("Parental Support", options=["None", "Low", "Moderate", "High", "Very High"], index=0)
ParentalEducation = st.selectbox("Parental Education", options=["None", "High School", "Some College", "Bachelor's", "Higher"], index=1)
Tutoring = st.selectbox("Tutoring", options=["Yes", "No"], index=0)
Sports = st.selectbox("Sports Participation", options=["Yes", "No"], index=0)
Extracurricular = st.selectbox("Extracurricular Activities", options=["Yes", "No"], index=0)
Music = st.selectbox("Music Interest", options=["Yes", "No"], index=0)
Volunteering = st.selectbox("Volunteering", options=["Yes", "No"], index=0)

# Convert categorical inputs to numerical values
sex_male = 1 if Gender == "Male" else 0
sex_female = 1 if Gender == "Female" else 0
ParentalSupport = {"None": 0, "Low": 1, "Moderate": 2, "High": 3, "Very High": 4}.get(ParentalSupport)
ParentalEducation = {"None": 0, "High School": 1, "Some College": 2, "Bachelor's": 3, "Higher": 4}.get(ParentalEducation)
Tutoring = 1 if Tutoring == "Yes" else 0
Sports = 1 if Sports == "Yes" else 0
Extracurricular = 1 if Extracurricular == "Yes" else 0
Music = 1 if Music == "Yes" else 0
Volunteering = 1 if Volunteering == "Yes" else 0

# Prepare input data as a list
student_data = [
    Age,
    sex_male,
    sex_female,
    ParentalEducation,
    StudyTimeWeekly,
    Absences,
    Tutoring,
    ParentalSupport,
    Extracurricular,
    Sports,
    Music,
    Volunteering
]

# Create dictionary for predicted Grade Class
GradeClass = {
    0: "You are on your way for an A!! >:) ",
    1: "You are on your way for a B :) ",
    2: "You are on your way for a C :/ ",
    3: "You are on your way for a D :(",
    4: "You are on your way for an F 0_0 *gulp*"
}

# Button to make a prediction
if st.button("Predict"):
    # Predict the grade class
    prediction = predict(student_data)

    # Display the prediction
    st.write(f"I predict only one thing -> {GradeClass[prediction]}")