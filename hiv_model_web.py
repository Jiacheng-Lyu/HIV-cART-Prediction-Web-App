#importing all the important libraries
import streamlit as st

import os
from collections import defaultdict
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "Clinical features","Combined clinical and proteome features"])

#Home Page 
if input_feature_type == "Home":
    st.title("the prediction App for the follow up response state of the cART")
    # st.image("Medical Prediction Home Page.jpg")
    st.text("The Following Predicted Features Are Available ->")
    st.text("1. Clinical features")
    st.text("2. Combined clinical and proteome features")
    st.text("")
    st.text("The Following Predicted Follow-up Windows Are Available ->")
    st.text("1. Less than 9 months")
    st.text("2. More than 9 months")

input_type_name_spaces = {'Clinical features': 'clinical', 'Combined clinical and proteome features': 'all'}
prediction_window_name_spaces = {'less-than-9': 'Less than 9 months', 'more-than-9': 'More than 9 months'}
respond_state_name_spaces = {1: 'Non Respond', 0: 'Respond'}

def return_predict_result(predict_out):
    for k, v in predict_out.items():
        if respond_state_name_spaces.get(v[0]) == 'Respond':
            st.success("You will Respond to the cART at the {} windows".format(k))
        else:
            st.warning("You will Not Respond to the cART at the {} windows".format(k))

def predict_state(input_feature_type, input_value):
    predict_out = {}
    for prediction_window in prediction_window_name_spaces:
        predict_out[prediction_window_name_spaces[prediction_window]] = models[input_type_name_spaces[input_feature_type]][prediction_window].predict(input_value)
    return predict_out


models = defaultdict(dict)
for f in os.listdir('./models'):
    if f.endswith('joblib'):
        name1, name2, *_ = f.split('_')
        models[name1][name2] = joblib.load(os.path.join('./models', f))


if input_feature_type == 'Clinical features':
    st.header("Predict whether you will respond to cART in the future")
    st.write("Providing two decimal place will make the prediction more accurate")

    age = st.number_input("The current age")
    age_first_cART = st.number_input("The age when you first accept the cART")
    cd4_L = st.number_input("The current count of CD4+ cells")
    cd4_B = st.number_input("The count of CD4+ cells when you first accept the cART")
    treatment_year = age - age_first_cART

    input_value = np.array([[cd4_B, cd4_L, age, treatment_year]])
    predict_out = predict_state(input_feature_type, input_value)

    if st.button("Predict"):
        return_predict_result(predict_out)


if input_feature_type == 'Combined clinical and proteome features':
    st.header("Predict whether you will respond to cART in the future")
    st.write("Providing two decimal place will make the prediction more accurate")

    age = st.number_input("The current age")
    age_first_cART = st.number_input("The age when you first accept the cART")
    cd4_L = st.number_input("The current count of CD4+ cells")
    cd4_B = st.number_input("The count of CD4+ cells when you first accept the cART")
    treatment_year = age - age_first_cART

    apol1 = st.number_input("The APOL1 protein expression level")
    ppbp = st.number_input("The PPBP protein expression level")
    acat2 = st.number_input("The ACAT2 protein expression level")

    input_value = np.array([[cd4_B, cd4_L, apol1, ppbp, acat2, age, treatment_year]])
    predict_out = predict_state(input_feature_type, input_value)

    if st.button("Predict"):
        return_predict_result(predict_out)
