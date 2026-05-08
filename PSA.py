import streamlit as st
from zxcvbn import zxcvbn

st.set_page_config(page_title="Password Strength Check", page_icon="🛡️")

st.title("🛡️ Is your password safe?")
st.write("You Can check how long a hacker would take to guess your password.")

user_password = st.text_input("Type a password here:", type="password")

if user_password:
    analysis = zxcvbn(user_password)
    
    time_to_crack = analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']
    strength_score = analysis['score']
    
    st.subheader(f"Time for a hacker to crack this: :blue[{time_to_crack}]")

    if strength_score <= 1:
        st.error("Rating: Very Weak 🚩")
    elif strength_score == 2:
        st.warning("Rating: Fair ⚠️")
    else:
        st.success("Rating: Strong ✅")
    
    st.progress((strength_score + 1) * 25 if strength_score < 4 else 100)

    st.write("### Suggestions to make it better:")
    suggestions = analysis['feedback']['suggestions']
    if suggestions:
        for tip in suggestions:
            st.write(f"* {tip}")
    else:
        st.write("Looking good! This password is hard to guess.")
st.markdown("---") # This adds a thin horizontal line
st.write("### Connect with me manojgolla2622@gmail.com")
st.write("**Developed by: [Golla Manoj]**")
st.write("Role: Aspiring SOC Analyst / Cybersecurity Specialist")

