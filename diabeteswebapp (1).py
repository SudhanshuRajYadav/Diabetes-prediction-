#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pickle
import streamlit as st

# loading the saved model and scaler
loaded_model=pickle.load(open("trained_model.sav","rb"))
loaded_scaler=pickle.load(open("scaler.sav","rb"))


# creating a function for prediction
def diabetes_prediction(input_data):

  # changing the input_data to numpy array of floats
  input_data_as_numpy_array=np.asarray(input_data, dtype=float)

  # reshape the  array as we are predicting for one instance
  input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)

  # standardize the input data
  std_data=loaded_scaler.transform(input_data_reshaped)
  # print(std_data)

  prediction = loaded_model.predict(std_data)
  print(prediction)

  if (prediction[0]==0):
    return'the person is not diabetic'
  else:
    return'the person is diabetic'


def main():
    # giving a title
    st.title('Diabetes Prediction Web App')
    # getting the input data from the user    
    pregnancies=st.text_input('Number of pregnancies')   
    Glucose=st.text_input('Glucose value')
    BloodPressure=st.text_input('BloodPressure value')  
    SkinThickness=st.text_input('SkinThickness value')  
    Insulin=st.text_input('Insulin value')  
    BMI=st.text_input('BMI value')  
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')  
    Age=st.text_input('Age of the person')  
    # code for prediction
    diagnosis= ""
    

# creating a button for prediction
    if st.button('diabetes Test Result'):
        diagnosis= diabetes_prediction([pregnancies,Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)   
if __name__ == '__main__':
    main()
