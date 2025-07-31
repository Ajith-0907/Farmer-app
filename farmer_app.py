#app.py

import streamlit as st

st.set_page_config(page_title="Farmer Support Chatbot", layout="centered")

# Knowledge base
knowledge_base = {
    "pests": {
        "keywords": ["pest", "insect", "bug", "infestation"],
        "response": "Common pests include aphids, caterpillars, and beetles. Use neem oil or insecticidal soap for organic control."
    },
    "diseases": {
        "keywords": ["disease", "fungus", "blight", "rot", "wilting"],
        "response": "Plant diseases can be fungal, bacterial, or viral. Use crop rotation, resistant varieties, and fungicides."
    },
    "fertilizer": {
        "keywords": ["fertilizer", "nutrient", "NPK", "manure", "compost"],
        "response": "Soil testing is best. Use compost/manure or balanced NPK like 10-10-10."
    },
    "weather": {
        "keywords": ["weather", "rain", "drought", "frost"],
        "response": "Check forecasts. Use drip irrigation for drought; row covers for frost."
    },
    "crop selection": {
        "keywords": ["crop", "plant", "variety", "selection"],
        "response": "Choose crops based on soil, climate, and market demand."
    },
    "irrigation": {
        "keywords": ["water", "irrigation", "drip", "sprinkler"],
        "response": "Use drip or sprinkler systems. Monitor soil moisture."
    },
    "default": {
        "response": "I couldn't understand. Please ask about pests, diseases, fertilizers, weather, crop selection, or irrigation."
    }
}

# Helper function
def get_response(message):
    message = message.lower()
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! I'm your farming assistant. How can I help you?"
    if any(word in message for word in ["thank", "thanks"]):
        return "You're welcome! Anything else you'd like to ask?"
    
    for topic, info in knowledge_base.items():
        if topic != 'default':
            if any(keyword in message for keyword in info['keywords']):
                return info['response']
    return knowledge_base['default']['response']


# Streamlit UI
st.title("🌱 Farmer Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role, text = msg
    with st.chat_message(role):
        st.markdown(text)

user_input = st.chat_input("Type your farming question...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)
    st.session_state.messages.append(("assistant", response))
    with st.chat_message("assistant"):
        st.markdown(response)
