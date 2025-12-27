import os
import streamlit as st
from datetime import datetime

from agent.travel_agent import create_travel_agent
from utils.guardrails import is_travel_related
from utils.language_helper import build_prompt


# Load OpenAI API Key securely
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# Greeting Messages (Multi-language)
GREETINGS = {
    "English": "Hello! 👋 I’m your AI Travel Assistant. How can I help you today?",
    "Hindi": "नमस्ते! 👋 मैं आपका AI ट्रैवल सहायक हूँ। मैं आपकी कैसे मदद कर सकता हूँ?",
    "Tamil": "வணக்கம்! 👋 நான் உங்கள் AI பயண உதவியாளர். நான் எப்படி உதவலாம்?",
    "Bengali": "নমস্কার! 👋 আমি আপনার AI ভ্রমণ সহকারী। আমি কীভাবে সাহায্য করতে পারি?"
}

# Initialize Trip History (Session-based)
if "history" not in st.session_state:
    st.session_state.history = []


# Streamlit Page Config
st.set_page_config(page_title="Agentic Travel Planner")


# Simple Font Styling
st.markdown(
    """
    <style>
    .big-font {
        font-size:22px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App Title
st.markdown(
    '<p class="big-font">🌍 Agentic AI Travel Planner</p>',
    unsafe_allow_html=True
)


#Greeting Language Selection
greeting_language = st.selectbox(
    "Select Greeting Language",
    ["English", "Hindi", "Tamil", "Bengali"]
)

st.markdown(
    f"<p class='big-font'>{GREETINGS[greeting_language]}</p>",
    unsafe_allow_html=True
)


# Communication Language Selection
# (Language in which agent will respond)
communication_language = st.selectbox(
    "Preferred Communication Language",
    [
        "English", "Hindi",
        "French", "German", "Spanish",
        "Tamil", "Telugu", "Kannada", "Malayalam", "Bengali"
    ]
)


# User Query Input
query = st.text_area(
    "Describe your trip",
    placeholder="Plan a 3-day trip from Delhi to Goa"
)


# Validate Query (Guardrails)
if query and not is_travel_related(query):
    st.warning(
        "⚠️ I can help only with travel planning, trips, flights, hotels, and budgets."
    )
    st.stop()



# Process Query Using Agent
if st.button("Plan My Trip"):

    with st.spinner("Planning your trip..."):

        # Convert query based on selected communication language
        final_prompt = build_prompt(query, communication_language)

        # Create agent
        agent = create_travel_agent()

        # Call agent (returns TEXT output)
        result = agent.invoke({"query": final_prompt})

        # Save Trip History (Safe & Correct)
        st.session_state.history.append({
            "query": query,
            "language": communication_language,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

    # Display Result
    st.success("Trip Planned Successfully!")
    st.markdown(result)


# Display Trip History
if st.session_state.history:
    st.subheader("📜 Trip History")
    st.table(st.session_state.history)
