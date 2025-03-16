
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Ramadan Assignment", layout="wide")

# Main title
st.title("Ramadan: Blessings, Mercy, and Virtues")

# Sidebar for Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Select a Topic:", ["Introduction", "Acts of Worship", "Fasting Benefits", "Ramadan's Message"])

# Introduction Section
if section == "Introduction":
    st.header("The Importance of Ramadan")
    st.write("""
    Ramadan is a sacred month in which the Quran was revealed. It is the most superior of all months.
    During this time, the doors of Paradise are opened, and the doors of Hell are closed.
    Laylatul Qadr, a night in this month, is better than a thousand months.
    Fasting is solely for Allah, and its reward is granted by Him alone.
    """)

# Acts of Worship in Ramadan
elif section == "Acts of Worship":
    st.header("Acts of Worship in Ramadan")
    st.markdown("""
    - *Giving Charity* - Supporting the needy and contributing to good causes.
    - *Helping Others* - Assisting and easing difficulties for others.
    - *Greeting with Salam and Smiling* - Spreading positivity and kindness.
    - *Engaging in Special Prayers* - Increasing devotion through extra prayers.
    - *Observing Obligatory Fasts* - Fulfilling the fundamental duty of fasting.
    - *Bringing Positive Change* - Strengthening character and discipline.
    - *Replacing Bad Habits with Good Ones* - Transforming lifestyle positively.
    - *Strengthening Obedience to Allah* - Increasing spiritual awareness and self-discipline.
    """)

# Benefits of Fasting
elif section == "Fasting Benefits":
    st.header("Spiritual and Physical Benefits of Fasting")
    st.markdown("""
    - *Fasting Will Intercede on the Day of Judgment* - It will plead for the believer.
    - *A Path to Success in the Hereafter* - A means to attain eternal rewards.
    - *Protection from Hellfire* - A safeguard against punishment.
    - *Forgiveness for Past Sins* - An opportunity to cleanse past mistakes.
    - *Spiritual and Physical Purification* - Strengthens both faith and body.
    - *Discipline and Self-Control* - Enhances patience, gratitude, and self-restraint.
    - *Reward for Nafl Prayer is Equal to an Obligatory Prayer* - Even the smallest good deed earns multiple rewards.
    """)

# Message of Ramadan
elif section == "Ramadan's Message":
    st.header("Message of Ramadan: Seeking Mercy and Forgiveness")
    st.write("""
    We are fortunate to witness Ramadan and engage in special worship. However, true success is in utilizing this month
    for seeking forgiveness and mercy. Ramadan offers a chance to draw closer to Allah, correct our ways, and improve ourselves.
    Let us value this sacred time and strive for spiritual growth and eternal success.
    """)
    