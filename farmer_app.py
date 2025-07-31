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

    general_responses = {
        "పురుగు": "పురుగుల నివారణకు సేంద్రియ నిమ్మ ఆయిల్ మరియు బవేరియా బాసియానా వాడడం మంచిది.",
        "వ్యాధి": "వ్యాధుల నివారణకు మాంకోజెబ్ మరియు కాపర్ ఆక్సీక్లోరైడ్ ఉపయోగించవచ్చు.",
        "ఎరువు": "పంటలకు అవసరమైన ఎరువులు: యూరియా, DAP మరియు సూపర్ ఫాస్ఫేట్.",
        "వాతావరణం": "ప్రస్తుత వాతావరణ పరిస్థితులను అనుసరించి సాగు చేయడం ఉత్తమం.",
        "నీరు": "నీటిని సమర్థవంతంగా వాడేందుకు డ్రిప్ లేదా స్ప్రింక్లర్ పద్ధతులు ఉపయోగించండి.",
        "drip": "డ్రిప్ ఇరిగేషన్ నీటి వినియోగాన్ని తగ్గించడానికి మరియు దిగుబడి పెంచడానికి సహాయపడుతుంది.",
        "sprinkler": "స్ప్రింక్లర్ పద్ధతి సమానంగా నీరు పంపిణీ చేస్తుంది మరియు పొలం కోసం మంచిది.",
        "water": "నీటి పొదుపు పద్ధతుల వాడకం అనివార్యం. డ్రిప్, స్ప్రింక్లర్ వంటివి ఉపయుక్తం.",
        "irrigation": "ఇరిగేషన్ పద్ధతులు మీ పొలానికి సరిపోయే విధంగా ఎంచుకోండి — డ్రిప్, ఫర్‌రో, స్ప్రింక్లర్."
    }

    general_links = {
        "పురుగు": "<br><a href='https://www.youtube.com/watch?v=tyqsbE8hslE' target='_blank'>👉 పురుగు నివారణ వీడియో</a>",
        "వ్యాధి": "<br><a href='https://www.youtube.com/watch?v=tDrx4Qgk1XE' target='_blank'>👉 వ్యాధి నివారణ వీడియో</a>",
        "ఎరువు": "<br><a href='https://www.youtube.com/watch?v=epMl43O3gts' target='_blank'>👉 ఎరువుల సమాచారం వీడియో</a>",
        "వాతావరణం": "<br><a href='https://www.youtube.com/watch?v=majAdTK7758' target='_blank'>👉 వాతావరణ సూచనలు వీడియో</a>",
        "నీరు": "<br><a href='https://www.youtube.com/watch?v=6At-n-B1Bjc' target='_blank'>👉 నీటిపారుదల వీడియో</a>",
        "drip": "<br><a href='https://www.youtube.com/watch?v=ikAoMn93mEw' target='_blank'>👉 Drip Irrigation System Video</a>"
    }

    keyword_pool = {
        "పురుగు": ["పురుగు", "ఇన్సెక్ట్", "చైతూ", "ఆఫిడ్స్"],
        "వ్యాధి": ["వ్యాధి", "ఫంగస్", "బ్లైట్", "విల్టింగ్"],
        "ఎరువు": ["ఎరువు", "పోషకాలు", "ఫెర్టిలైజర్", "యూరియా"],
        "వాతావరణం": ["వాతావరణం", "వర్షం", "కరువు", "మౌసమ్"],
        "నీరు": ["నీరు", "డ్రిప్", "ఇరిగేషన్", "sprinkler", "పంపిణీ"],
        "drip": ["డ్రిప్", "డ్రిప్ ఇరిగేషన్"],
        "sprinkler": ["స్ప్రింక్లర్"],
        "water": ["నీరు", "నీటి పంపిణీ"],
        "irrigation": ["ఇరిగేషన్", "నీటి పద్ధతులు"]
    }

    for key, keywords in keyword_pool.items():
        if any(kw in message for kw in keywords):
            return general_responses[key] + general_links.get(key, "")

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
