# code streamlit is installed
# cmd for run streamlit  """streamlit run Streamlit/demo1.py"""
from cmath import cos
from inspect import GEN_CLOSED
import streamlit as st  

st.title("Streamlit Demo")
st.header("streamlit is awesom")
st.subheader("streamlit")
st.text("ST")
st.markdown("ST as Streamlit")
st.success("success")
st.info("Info")
st.warning("warning")
st.error("Error")
st.exception("Exception")
# st.balloons()
st.button('Register')

#media element
st.image("ui/hero.png")
st.image("ui/player.png")

#st.video(r"video link here") we can use video also copy youtube url also
# st.audio(r" ")


# Add widgets
name = st.text_input("Enter username")
cost = st.number_input("Enter the cost")
status = st.checkbox("Save")
gender = st.radio("Gender",["male", "Female", "Others"])
querylist = ["How to use streamlit", 
        "How to run streamlit", 
        "How to install sytreamlit"]
query = st.selectbox("What is query", querylist)    

btn = st.button("Submit the response")

if btn:
    st.write("Username", name)
    st.write("Cost",cost)
    st.write("Status", status)
    st.write("gender",gender)
    st.write("Query", query)
