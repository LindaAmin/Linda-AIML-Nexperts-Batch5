import streamlit as st

st.title("First Streamlit app")

st.write("Helloww. I am here to build apps!")

name = st.text_input("What is your name?")
age = st.slider("How old are you?", 1, 100, 25)
if name:
    st.write(f"Nice to meet you {name}")


import pandas as pd
data = {
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Cups of Coffee": [1, 2, 4, 3, 5]
}
coffee_table = pd.DataFrame(data)
st.write("Here is the data:")
st.dataframe(coffee_table)


st.write("Here is the visual chart:")
st.bar_chart(coffee_table, x="Days", y="Cups of Coffee", color = "#008321")

st.divider() # adds a horizontal line

name2 = st.text_input("What is your name????")
feedback = st.text_area("Leave your comments here:")

age = st.number_input("Enter your age??:", min_value=0, max_value=120)
temperature = st.slider("Select the temperature", 0, 100, 50)

st.divider()

size = st.radio("Pick a size:", ["Small", "Medium", "Large"])
country = st.selectbox("Where are you from?", ["India", "Malaysia", "USA", "UK"])
skills = st.multiselect("Select your skills:", ["Python", "SQL", "Power BI", "AI"])

# boolean
agree = st.checkbox("I agree to the terms")


st.divider()
dark_mode = st.toggle("Enable Dark Mode")

st.button("Click me")



