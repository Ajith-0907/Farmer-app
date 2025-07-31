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

    general_keywords = {
        "పురుగు": "పురుగుల నివారణకు నిమ్మఆయిల్, బవేరియా బాసియానా వాడండి. [👉 వీడియో](https://www.youtube.com/watch?v=AieFCNubgVg)",
        "వ్యాధి": "వ్యాధుల నివారణకు కార్బెండజిమ్, మాంకోజెబ్ వాడండి. [👉 వీడియో](https://www.youtube.com/watch?v=tDrx4Qgk1XE)",
        "ఎరువు": "పొలం ఎరువులలో 10-26-26, యూరియా వాడవచ్చు. [👉 వీడియో](https://www.youtube.com/watch?v=epMl43O3gts)",
        "వాతావరణం": "వాతావరణ పరిస్థితుల్ని గమనించి సాగు ప్లాన్ చేయండి. [👉 సూచనలు](https://www.youtube.com/watch?v=tE1jvpwmyiU)",
        "నీరు": "డ్రిప్ లేదా స్ప్రింక్లర్ పద్ధతులు నీటి వినియోగం తగ్గిస్తాయి. [👉 వీడియో](https://www.youtube.com/watch?v=6At-n-B1Bjc)"
    }

    for key, reply in general_keywords.items():
        if key in message:
            return reply

    for crop, details in crop_tips.items():
        crop_keywords = crop.lower().replace("(", "").replace(")", "").split()
        if any(word in message for word in crop_keywords):
            return details

    return "క్షమించండి, మీ ప్రశ్నకు సరైన సమాచారం లభించలేదు. మీరు మరో రీతిలో ప్రయత్నించండి లేదా క్రింద ఉన్న పంటల జాబితా చూడండి."

# Layout
st.title("🌾 రైతు సహాయక చాట్‌బాట్")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    <style>
body, .stApp {
    background-color: #f9f9f9;
    color: #111;
}
.chat-bubble {
    border-radius: 15px;
    padding: 10px 15px;
    margin: 10px 0;
    display: inline-block;
    max-width: 80%;
    font-size: 0.9rem;
}
.user {
    background-color: #d0e8ff;
    color: #000;
    margin-left: auto;
    text-align: right;
    border-bottom-right-radius: 5px;
}
.bot {
    background-color: #f1f1f1;
    color: #000;
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
