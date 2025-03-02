import streamlit as st
import math
import joblib

model = joblib.load('titanic.pkl')

st.set_page_config('Survival State of Passengers in the Titanic Ship', page_icon="💡", layout='wide')
st.header('🤔Survival State of Passenger in the Titanic Ship')
st.markdown('This app predicts the survival state of passengers who were in the Titanic Ship')


col1, col2, col3, col4 = st.columns(4)
with col1:
    PassengerId = st.number_input("Input the ID number of the passenger. NB: numbers only")
with col2:
    Pclass = st.selectbox("Class of Passenger",("Premiere","Executive","Economy"))
with col3:
    Sex = st.selectbox("Gender",("Male","Female")) 
with col4:
    Age = st.number_input("Age of passenger")


col5, col6, col7 = st.columns(3)

with col5:
    SibSp = st.number_input("Input the number of Siblings/Spouses")
with col6:
    Parch = st.number_input("Input the number of Parents/Children")
with col7:
    Fare = st.number_input("Input the fare of the Journey")

if st.button("Predict"):
    pclass = 1
    if Pclass=="Economy":
        pclass = 3
    elif Pclass=="Executive":
        pclass = 2
    
    gender = 0
    if Sex=="Female":
        gender=1
    PassengerId = int(PassengerId)
    age = math.ceil(Age)
    sibsp = math.ceil(SibSp)
    parch = math.ceil(Parch)
    fare = math.ceil(Fare)

    
    result = model.predict([[PassengerId, pclass,gender,age,sibsp,parch,fare]])
    output_labels = {1: "The passenger will Survive", 
                     0: "The passenger will not survive"}
    st.markdown(f"## {output_labels[result[0]]}")

# Add Additional Information Section
st.markdown("---")
st.subheader("💡 About This App")
st.write("""This app predicts predicts the survival state of passengers in the titanic ship. 
Simply input the details above to see the state of the passenger""")






