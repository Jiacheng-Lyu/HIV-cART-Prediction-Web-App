#importing all the important libraries
import streamlit as st

import os
from collections import defaultdict
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "Clinical features","Proteome features","Combined clinical and proteome features"])

#Home Page 
if input_feature_type == "Home":
    st.title("the prediction App for the follow up response state of the cART")
    # st.image("Medical Prediction Home Page.jpg")
    st.text("The Following Predicted Features Are Available ->")
    st.text("1. Clinical features")
    st.text("2. Proteome features")
    st.text("3. Combined clinical and proteome features")
    st.text("")
    st.text("The Following Predicted Follow-up Windows Are Available ->")
    st.text("1. 3 to 6 months")
    st.text("2. 6 to 9 months")
    st.text("3. 9 to 12 months")
    st.text("3. More than 12 months")



input_type_name_spaces = {'Clinical features': 'clinical', 'Proteome features': 'proteome', 'Combined clinical and proteome features': 'all'}
prediction_window_name_spaces = {'3to6': '3 to 6 months', '6to9': '6 to 9 months', '9to12': '9 to 12 months', 'more-than-12': 'More than 12 months'}
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

    input_value = np.array([[cd4_L, age, cd4_B, treatment_year]])
    predict_out = predict_state(input_feature_type, input_value)

    if st.button("Predict"):
        return_predict_result(predict_out)

if input_feature_type == 'Proteome features':
    st.header("Predict whether you will respond to cART in the future")
    st.write("Providing two decimal place will make the prediction more accurate")

    apol1 = st.number_input("The APOL1 protein expression level")
    acaca = st.number_input("The ACACA protein expression level")
    serpind1 = st.number_input("The SERPIND1 protein expression level")
    myh14 = st.number_input("The MYH14 protein expression level")
    pkm = st.number_input("The PKM protein expression level")
    syne1 = st.number_input("The SYNE1 protein expression level")

    input_value = np.array([[apol1, acaca, serpind1, myh14, pkm, syne1]])
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
    acaca = st.number_input("The ACACA protein expression level")
    serpind1 = st.number_input("The SERPIND1 protein expression level")
    myh14 = st.number_input("The MYH14 protein expression level")
    pkm = st.number_input("The PKM protein expression level")
    syne1 = st.number_input("The SYNE1 protein expression level")

    input_value = np.array([[apol1, acaca, serpind1, cd4_L, age, cd4_B, myh14, pkm, syne1, treatment_year]])
    predict_out = predict_state(input_feature_type, input_value)

    if st.button("Predict"):
        return_predict_result(predict_out)
