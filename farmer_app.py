import streamlit as st

st.set_page_config(page_title="రైతు సహాయక చాట్‌బాట్", layout="wide")

# Static crop prices and trend (simulated)
crop_prices = {
    "వరి (Rice)": (2100, "⬆️", 2020),
    "కాటన్ (Cotton)": (6200, "⬇️", 6300),
    "మిరప (Chilli)": (9000, "⬆️", 8800),
    "జొన్న (Jowar)": (2500, "⬇️", 2600),
    "సెనగ (Chana)": (5400, "⬆️", 5300)
}

# Crop-specific help with updated verified YouTube links
crop_tips = {
    "వరి (Rice)": (
        "పురుగు నివారణకు: కార్టాప్ హైడ్రోక్లోరైడ్, మాంకోజెబ్.<br>"
        "<a href='https://www.youtube.com/watch?v=TYY3pe5pNCU' target='_blank'>🌾 Rice Cultivation Video</a>"
    ),
    "కాటన్ (Cotton)": (
        "కాటన్ వ్యాధుల నివారణకు: neem oil, imidacloprid.<br>"
        "<a href='https://www.youtube.com/watch?v=SJPLi2AJifA' target='_blank'>🧪 Cotton Pest Control</a>"
    ),
    "మిరప (Chilli)": (
        "మిరప చేలో ఫంగల్ వ్యాధుల నివారణకు: carbendazim, azoxystrobin.<br>"
        "<a href='https://www.youtube.com/watch?v=bDKs4YvVPc4' target='_blank'>🌶️ Chilli Farming Process</a>"
    ),
    "జొన్న (Jowar)": (
        "జొన్నకు neem spray వాడాలి.<br>"
        "<a href='https://www.youtube.com/watch?v=spTvur2Pvqg' target='_blank'>🌽 Jowar Farming Process</a>"
    ),
    "సెనగ (Chana)": (
        "సెనగకు early blight నివారణకు Mancozeb వాడండి.<br>"
        "<a href='https://www.youtube.com/watch?v=qs2JnBFYcdw' target='_blank'>🥜 Chana Farming Guide</a>"
    )
}

# Chatbot response logic (unchanged)
def get_response(message):
    message = message.lower()
    if any(word in message for word in ["హాయ్", "హలో", "నమస్తే"]):
        return "హలో! నేను మీ వ్యవసాయ సహాయకుడు. ఎలా సహాయం చేయగలను?"
    if any(word in message for word in ["ధన్యవాదాలు", "ధన్యవాదం", "థ్యాంక్స్"]):
        return "మీకు స్వాగతం! ఇంకా ఏవైనా సందేహాలు ఉన్నాయా?"
    return "దయచేసి మీ వ్యవసాయ సంబంధిత ప్రశ్నను తెలుగులో టైప్ చేయండి."

# Layout
st.title("🌾 రైతు సహాయక చాట్‌బాట్")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <style>
    .chat-bubble {
        border-radius: 15px;
        padding: 10px 15px;
        margin: 10px 0;
        display: inline-block;
        max-width: 80%;
        font-size: 0.9rem;
    }
    .user {
        background-color: #e3f2fd;
        margin-left: auto;
        text-align: right;
        border-bottom-right-radius: 5px;
    }
    .bot {
        background-color: #f1f1f1;
        margin-right: auto;
        text-align: left;
        border-bottom-left-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...")
    if user_input:
        st.session_state.messages.append(("user", user_input))
        st.session_state.messages.append(("bot", get_response(user_input)))

    for role, text in st.session_state.messages:
        css_class = "user" if role == "user" else "bot"
        st.markdown(f"<div class='chat-bubble {css_class}'>{text}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("## 📌 పంటలు")
    for crop, tip in crop_tips.items():
        with st.expander(crop):
            st.markdown(tip, unsafe_allow_html=True)
            price, trend, yesterday = crop_prices.get(crop, ("–", "", "–"))
            st.markdown(f"<small><b>ప్రస్తుత ధర:</b> ₹{price} {trend} (నిన్న ₹{yesterday})</small>", unsafe_allow_html=True)
