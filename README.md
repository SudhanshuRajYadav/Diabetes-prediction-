# Diabetes-prediction-
An Data Science project using # training the model classifier (SVC(kernel='linear')) with Accuracy score of the training data: 0.7866449511400652,accuracy score of the test data: 0.7727272727272727,Dataset size(diabetic person) is 768 rows 9 columns
# 🩺 Diabetes Prediction Using Machine Learning

## 📌 Project Overview

This project is a complete **Data Science and Machine Learning solution** that predicts whether a person is likely to have diabetes based on medical attributes. The project follows a real-world data science workflow used in organizations, starting from data collection and cleaning to model training, evaluation, and deployment through an interactive Streamlit web application.

The objective is to help healthcare professionals and individuals identify potential diabetes risk using machine learning techniques.

---

## 🎯 Business Problem

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help in timely diagnosis and preventive healthcare measures.

This project aims to build a machine learning model that can accurately predict diabetes based on patient health information and provide instant predictions through a user-friendly web application.

---

## 📂 Dataset

The project uses the **Diabetes Dataset**, which contains medical information of patients and a target variable indicating whether the patient has diabetes.

### Features

* Pregnancies
* Glucose
* Blood Pressure
* Skin Thickness
* Insulin
* BMI (Body Mass Index)
* Diabetes Pedigree Function
* Age

### Target Variable

* **Outcome**

  * 0 = Non-Diabetic
  * 1 = Diabetic

---

## 🛠 Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Pickle
* Streamlit
* Jupyter Notebook

---

## 🔄 Project Workflow

### 1. Data Collection

* Loaded the diabetes dataset using Pandas.
* Examined dataset structure and feature information.

### 2. Data Cleaning

* Checked for missing values.
* Verified data types.
* Removed inconsistencies and prepared data for analysis.

### 3. Exploratory Data Analysis (EDA)

* Analyzed feature distributions.
* Examined relationships between variables.
* Identified important health indicators affecting diabetes prediction.

### 4. Data Preparation

* Split data into training and testing datasets.
* Prepared features and target variables for machine learning.

### 5. Model Building

* Trained a machine learning classification model using Scikit-Learn.
* Learned patterns from historical patient data.

### 6. Model Evaluation

* Tested the model on unseen data.
* Measured prediction performance and reliability.

### 7. Model Saving

* Saved the trained model using Pickle for future use.

### 8. Web Application Development

* Built an interactive Streamlit application.
* Users can enter patient health details and receive instant predictions.

---

## 📊 Project Structure

```text
Diabetes_Prediction/
│
├── diabetes.csv
├── diabetes.ipynb
├── diabeteswebapp.py
├── trained_model.sav
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/SudhanshuRajYadav/Diabetes-prediction-.git
```

### Navigate to Project Folder

```bash
cd Diabetes_Prediction
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run diabeteswebapp.py
```

### Open in Browser

```text
http://localhost:8501
```

---

## 📈 Expected Workflow

1. Enter patient information.
2. Click **Diabetes Test Result**.
3. Model processes the input data.
4. Prediction is generated instantly.
5. User receives diabetes risk prediction.

---

## 📋 Results

* Successfully developed a machine learning model for diabetes prediction.
* Built an interactive Streamlit application for real-time predictions.
* Automated the prediction process using a trained machine learning model.
* Demonstrated the complete data science lifecycle from raw data to deployment.

---

## 💡 Key Learnings

* Data Cleaning using Pandas
* Exploratory Data Analysis (EDA)
* Feature Understanding
* Machine Learning Model Training
* Model Testing and Evaluation
* Model Serialization using Pickle
* Building Interactive Applications with Streamlit
* End-to-End Data Science Project Development

---

## 🔮 Future Improvements

* Improve model accuracy using advanced algorithms.
* Perform hyperparameter tuning.
* Add additional healthcare features.
* Deploy the application on Render or Streamlit Cloud.
* Integrate database support for storing prediction history.
* Enhance UI/UX for a better user experience.

---

## 👨‍💻 Conclusion

This project demonstrates a complete end-to-end **Data Science and Machine Learning workflow** for diabetes prediction. It showcases practical skills in data preprocessing, exploratory analysis, model development, evaluation, and deployment through a Streamlit web application, making it a strong portfolio project for Data Science and Machine Learning roles.
