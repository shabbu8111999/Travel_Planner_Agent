# 🌍 TripSage – Intelligent Travel Planning Assistant

TripSage is an **Agentic AI–based Travel Planning Assistant** built using **LangChain, OpenAI, and Streamlit**.  
It helps users plan trips intelligently by generating **personalized itineraries**, **budget estimates**, and **travel suggestions**, while supporting **multiple languages**, **session-based history**, and **user-friendly interactions**.

This project demonstrates **agentic reasoning**, **clean modular design**, and **production-style Streamlit UI**, making it suitable for **capstone evaluation, live demos, and resume projects**.

---

## 📌 Problem Statement

Planning a trip involves comparing flights, hotels, places to visit, weather conditions, and budgets across multiple platforms.  
This process is time-consuming, inconsistent, and often confusing.

**TripSage** solves this by acting as an **intelligent travel agent** that:
- Understands user intent
- Plans trips step-by-step
- Generates clear and readable itineraries
- Works across multiple languages
- Maintains trip history during the session

---

## 🎯 Project Objectives

### Primary Objectives
- Build an AI-powered travel planner using **LangChain**
- Generate:
  - Flight selection
  - Hotel recommendation
  - Day-wise itinerary
  - Weather summary
  - Budget breakdown
- Support multilingual users
- Provide a clean and readable Streamlit interface

### Secondary Objectives
- Add intent guardrails to block irrelevant queries
- Maintain session-based trip history
- Follow modular, industry-style project structure
- Ensure code clarity and maintainability

---

## 🧠 Key Features

- 🤖 **Agentic AI Planning** – Step-by-step reasoning using LLMs  
- 🌐 **Multi-language Support** – English, Hindi, Tamil, Bengali + more  
- 🧭 **User-Friendly Greeting Flow** – Language-based greeting experience  
- 🛡️ **Query Guardrails** – Handles only travel-related queries  
- 📜 **Session-Based Trip History** – View previously planned trips  
- 🎨 **Readable UI** – Large fonts and clean layout for better UX  

---

## 🧰 Tech Stack

- **Python**
- **LangChain (Core + OpenAI)**
- **OpenAI GPT-4o-mini**
- **Streamlit**
- **Session State Management**
- **HTML/CSS (for UI readability)**

---

## 📁 Project Structure

agentic_travel_planner/

│

├── app.py # Streamlit UI

│

├── agent/

│ └── travel_agent.py # AI planning logic

│

├── tools/

│ ├── flight_tools.py # Flight data logic

│ ├── hotel_tools.py # Hotel data logic

│ ├── places_tools.py # Places logic

│ ├── weather_tools.py # Weather API logic

│ └── budget_tools.py # Budget calculation

│

├── utils/

│ ├── data_loader.py # Load the data

│ ├── guardrails.py # Intent validation

│ └── language_helper.py # Multi-language handling

│

├── requirements.txt

└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <repository_link>
cd agentic_travel_planner
```

### 2️⃣ Initialize Environment and Added the Requirements (Using uv)
```bash
uv init
uv add streamlit openai langchain-core langchain-openai requests python-dotenv
```

### 3️⃣ Set OpenAI API Key

- Create the following file:

```bash
.streamlit/secrets.toml
```

- Add:

```bash
OPENAI_API_KEY = "Your OPENAI_API_KEY here"
```

### Run the Application
```bash
uv run streamlit run app.py
```

---

## 🖥️ How the Application Works
- User selects greeting language
- User selects communication language
- User enters a travel-related query
- Guardrails validate the query
- AI agent plans the trip
- Results are displayed in a readable format
- Trip details are stored in session-based history

---

## 🛡️ Guardrails & Safety
- Only travel-related queries are processed
- Non-relevant queries are politely rejected
- Prevents misuse of the AI agent

---

## 🌐 Multi-language Support
- User queries are internally processed in English
- Final responses are returned in the selected language

### Supported Languages
- Primary: English, Hindi
- Secondary: French, German, Spanish
- Indian Languages: Tamil, Telugu, Kannada, Malayalam, Bengali

---

## 📜 Trip History
- Stored using Streamlit session state
- Displays:
    - **User query**
    - **Preferred language**
    - **Timestamp**
- Automatically resets on page refresh (evaluation-friendly)

---

## 📈 Future Enhancements
- Tool-calling agent with real datasets
- Persistent storage (SQLite / JSON)
- Map-based itinerary visualization
- PDF export of travel plans
- User authentication

---

## 🎓 Evaluation Highlights
- Clean modular architecture
- Proper separation of UI, agent logic, and utilities
- Agentic reasoning demonstrated clearly
- Industry best practices followed
- Easy to explain and demo live

---

## 👤 Author

### ***TripSage – Intelligent Travel Planning Assistant***
### ***Built as an Agentic AI Capstone Project using LangChain and Streamlit.***

---

## ✅ Conclusion

### TripSage showcases how Agentic AI systems can simplify complex real-world problems like travel planning. The project balances technical correctness, user experience, and evaluation readiness, making it a strong demonstration of modern AI engineering practices.