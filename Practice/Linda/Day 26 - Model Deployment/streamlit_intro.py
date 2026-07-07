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
st.write ("Here is the data:")
st.dataframe(coffee_table)


st.write("here is the visual chart:")
st.bar_chart(coffee_table, x="Days", y="Cups of Coffee", color = "#006400")

st.divider() # adds a horizontal line

# ways to take inputs from users

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

show_password = st.toggle("SHOW Pass!!!")
if show_password:
    st.write ("This is the password: PASSWORD")
else:
    st.write("Nothing to see here")


dark_mode = st.toggle("Enable Dark Mode")

st.button("Click me")

if st.button("Test System"):
    st.success ("System is working flawlessly")
    st.info("Fun Fact: System was good yesterday, until you showed up!!!")
    st.warning ("If you keep doing this, I am going to fire you!!!")
    st.error ("Nuclear Failure. I am just kidding")

# Buttons with celebrate themes
if st.button("Hurray!!!. We lost the match with Spain!!!"):
    st.balloons()
    st.snow()

import time
if st.button ("Timer"):
    # loading animation
    with st.spinner ("making cofee for ya. Wait for it!!!"):
        time.sleep(3)
        st.success ("Coffee is mADE. So this is your day!!!")

import streamlit as st

if st.button ("Show Table"):
    st.toast("We fetched the table successfully!!!")
    st.dataFrame(coffee_table)

st.divider()
check_robot = st.text_input("What is 5 + 6")

if check_robot == "11":
    st.success ("You are human!!!")

else:
    