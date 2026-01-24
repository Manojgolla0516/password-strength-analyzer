import streamlit as st
from zxcvbn import zxcvbn

# This makes the website look professional
st.set_page_config(page_title="Password Strength Tool", page_icon="🛡️")

# --- MAIN PAGE ---
st.title("🛡️ Is your password safe?")
st.write("This tool checks how long a hacker's computer would take to guess your password.")

# Create the input box
user_password = st.text_input("Type a password here:", type="password")

if user_password:
    # Ask the 'zxcvbn' brain to analyze the password
    analysis = zxcvbn(user_password)
    
    # Get the hacking time and the score (0 to 4)
    time_to_crack = analysis['crack_times_display']['offline_fast_hashing_1e10_per_second']
    strength_score = analysis['score']
    
    # Show the result in a big blue box
    st.subheader(f"Time for a hacker to crack this: :blue[{time_to_crack}]")

    # Show a progress bar based on strength
    if strength_score <= 1:
        st.error("Rating: Very Weak 🚩")
    elif strength_score == 2:
        st.warning("Rating: Fair ⚠️")
    else:
        st.success("Rating: Strong ✅")
    
    st.progress((strength_score + 1) * 25 if strength_score < 4 else 100)

    # Give the user advice
    st.write("### Suggestions to make it better:")
    suggestions = analysis['feedback']['suggestions']
    if suggestions:
        for tip in suggestions:
            st.write(f"* {tip}")
    else:
        st.write("Looking good! This password is hard to guess.")

# --- FOOTER SECTION (ADD YOUR NAME HERE) ---
st.markdown("---") # This adds a thin horizontal line
st.write("### Connect with me manojgolla2622@gmail.com")
st.write("**Developed by: [Golla Manoj]**")
st.write("Role: Aspiring SOC Analyst / Cybersecurity Specialist")
