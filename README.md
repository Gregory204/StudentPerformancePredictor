# Student Performance Prediction (Data Science) 🎓

## Overview :books:

This project aims to predict student performance (GradeClass) based on various features such as age, gender, parental education, study time, absences, and extracurricular activities using a RandomForestClassifier model. This model is built without using GPA as a feature. It helps us to see what factors other than GPA might influence student grades.

## Dataset 💾

The project uses the "Students Performance Dataset" available on Kaggle. The dataset includes information about students' demographics, academic habits, and performance indicators.

## Features 📊

**Selected Features:**

* Age 
* Gender (sex\_male, sex\_female)
* Parental Education
* Study Time Weekly
* Absences
* Tutoring
* Parental Support
* Extracurricular Activities
* Sports
* Music
* Volunteering

**Target Variable:**

* GradeClass:  
    * 0: 'A' (GPA >= 3.5)
    * 1: 'B' (3.0 <= GPA < 3.5)
    * 2: 'C' (2.5 <= GPA < 3.0)
    * 3: 'D' (2.0 <= GPA < 2.5)
    * 4: 'F' (GPA < 2.0)

## Model 🤖

A RandomForestClassifier model is used for prediction. GridSearchCV is employed to find the best hyperparameters for the model, ensuring optimal performance.

## Usage 💻

1. **Data Preparation:**
   - Load the dataset using `pd.read_csv('/content/Student_performance_data _.csv')`.
   - Preprocess the data as shown in the notebook, including creating dummy variables for categorical features and rounding numerical features.

2. **Model Training:**
   - Split the data into training and testing sets.
   - Train the RandomForestClassifier model using the training data and the best hyperparameters found through GridSearchCV.

3. **Prediction:**
   - Create a DataFrame with the desired features for prediction.
   - Use the trained model to predict the GradeClass.

## Results :chart_with_upwards_trend:

The model's performance is evaluated using accuracy, precision, recall, and F1 scores.  The results obtained without including GPA as a predictor provide insights into the relative importance of other features. Cross-validation techniques are applied to mitigate overfitting.

![Train Vs Test Accuracy](https://github.com/user-attachments/assets/a36299bc-d043-4aec-a424-10f7dcfee40f)
![Train Vs Test Precision](https://github.com/user-attachments/assets/36a9ab7a-f5e8-4e10-b6fa-ebc930ca89ab)
![Train Vs Test Recall](https://github.com/user-attachments/assets/b60543c1-ba42-407b-b194-e00cfd8a10a6)

## Conclusion :bulb:

This project demonstrates the use of machine learning for student performance prediction. While achieving a high accuracy without relying on GPA can be a challenge, the model provides valuable insights into the factors that contribute to student success. Further improvements could involve exploring other models and optimizing feature selection strategies.

## Requirements 🔧

* Python 3
* Pandas
* Scikit-learn
* Seaborn

## Contributing 🤝

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
