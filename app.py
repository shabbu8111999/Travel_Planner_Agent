import os
import streamlit as st
from datetime import datetime

from agent.travel_agent import create_travel_agent
from utils.guardrails import is_travel_related
from utils.language_helper import build_prompt


# Streamlit Page Config
st.set_page_config(page_title="Agentic Travel Planner")


# Load OpenAI API Key securely
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


# Initialize Trip History (Session-based)
if "history" not in st.session_state:
    st.session_state.history = []

# Greeting Messages (Multi-language)
GREETINGS = {
    "English": "Hello! 👋 I’m your AI Travel Assistant. How can I help you today?",
    "Hindi": "नमस्ते! 👋 मैं आपका AI ट्रैवल सहायक हूँ। मैं आपकी कैसे मदद कर सकता हूँ?",
    "Tamil": "வணக்கம்! 👋 நான் உங்கள் AI பயண உதவியாளர். நான் எப்படி உதவலாம்?",
    "Bengali": "নমস্কার! 👋 আমি আপনার AI ভ্রমণ সহকারী। আমি কীভাবে সাহায্য করতে পারি?"
}

# Simple Font Styling
st.markdown(
    """
    <style>
    .stApp { font-size: 18px; }

    .app-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .readable-text {
        font-size: 20px;
        line-height: 1.6;
    }

    .success-text {
        font-size: 22px;
        font-weight: 600;
        margin-top: 15px;
    }

    .greeting-text {
        font-size: 22px;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# App Title
st.markdown(
    '<div class="app-title">TripSage – Your Intelligent Travel Guide 🪄</div>',
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
    st.markdown(
        '<div class="success-text">✅ Trip Planned Successfully!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="readable-text">{result}</div>',
        unsafe_allow_html=True
    )

# Display Trip History
if st.session_state.history:
    st.markdown(
        '<div class="section-title">📜 Trip History</div>',
        unsafe_allow_html=True
    )
    st.table(st.session_state.history)
