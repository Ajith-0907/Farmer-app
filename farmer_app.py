import streamlit as st

st.set_page_config(page_title="రైతు సహాయక చాట్‌బాట్", layout="centered")

# Telugu knowledge base with additional info and YouTube links
knowledge_base = {
    "pests": {
        "keywords": ["పెస్ట్", "పురుగులు", "ఇన్సెక్ట్", "ఇన్ఫెస్టేషన్"],
        "response": "సాధారణ పురుగుల్లో ఆఫిడ్స్, చైతూనిరుగులు, బీట్‌ల్స్ ఉంటాయి. నివారణకు: నీమ్ ఆయిల్, ట్రైకోగ్రామా, మరియు బవేరియా బాసియానా. [పురుగు నివారణ వీడియో](https://www.youtube.com/watch?v=AKfUZzXzfnU)"
    },
    "diseases": {
        "keywords": ["వ్యాధి", "ఫంగస్", "బ్లైట్", "రాట్", "విల్టింగ్"],
        "response": "వ్యాధుల నివారణకు: కార్బెండజిమ్, మాంకోజెబ్, కాపర్ ఆక్సీక్లోరైడ్ వాడవచ్చు. [వ్యాధి నియంత్రణ వీడియో](https://www.youtube.com/watch?v=7VqlgkSSmIE)"
    },
    "fertilizer": {
        "keywords": ["ఫెర్టిలైజర్", "పోషకాలు", "ఎన్‌పీకే", "మనం", "కాంపోస్ట్"],
        "response": "సాధారణంగా ఉపయోగించే ఎరువులు: 10-26-26, యూరియా, సూపర్ ఫాస్ఫేట్. [ఎరువుల ఉపయోగం వీడియో](https://www.youtube.com/watch?v=epMl43O3gts)"
    },
    "weather": {
        "keywords": ["వాతావరణం", "వర్షం", "కరువు", "చలికాలం"],
        "response": "వాతావరణాన్ని గమనిస్తూ సాగు ప్లాన్ చేసుకోండి. వర్షాకాలం లో మురుగు నీరు నిలవకుండా చూడాలి. [వాతావరణ సాగు చిట్కాలు](https://www.youtube.com/watch?v=tE1jvpwmyiU)"
    },
    "crop selection": {
        "keywords": ["పంట", "విత్తనాలు", "ఎంపిక", "కృషి"],
        "response": "రైతులకు అనువైన పంటలు: వరి, మక్కజొన్న, కంది. స్థానిక మార్కెట్ డిమాండ్ ఆధారంగా ఎంచుకోండి. [పంట ఎంపిక వీడియో](https://www.youtube.com/watch?v=5CvWyCGZKoo)"
    },
    "irrigation": {
        "keywords": ["నీరు", "ఇరిగేషన్", "డ్రిప్", "స్ప్రింక్లర్"],
        "response": "డ్రిప్, స్ప్రింక్లర్, ఫురో తరహా పద్ధతులు. [ఇరిగేషన్ సిస్టమ్ వీడియో](https://www.youtube.com/watch?v=6At-n-B1Bjc)"
    },
    "default": {
        "response": "క్షమించండి, నేను మీ ప్రశ్నను అర్థం చేసుకోలేకపోయాను. దయచేసి పురుగులు, వ్యాధులు, ఎరువులు, వాతావరణం, పంట ఎంపిక లేదా నీటిపారుదల గురించి అడగండి."
    }
}

# Logic to get response
def get_response(message):
    message = message.lower()
    if any(word in message for word in ["హాయ్", "హలో", "నమస్తే"]):
        return "హలో! నేను మీ వ్యవసాయ సహాయకుడు. ఎలా సహాయం చేయగలను?"
    if any(word in message for word in ["ధన్యవాదాలు", "ధన్యవాదం", "థ్యాంక్స్"]):
        return "మీకు స్వాగతం! ఇంకా ఏవైనా సందేహాలు ఉన్నాయా?"

    for topic, info in knowledge_base.items():
        if topic != 'default':
            if any(keyword in message for keyword in info['keywords']):
                return info['response']
    return knowledge_base['default']['response']

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🌾 రైతు సహాయక చాట్‌బాట్")
st.markdown("""
<style>
.chat-bubble {
    border-radius: 15px;
    padding: 10px 15px;
    margin: 10px 0;
    display: inline-block;
    max-width: 80%;
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

# Display previous messages
for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='chat-bubble user'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot'>{text}</div>", unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = get_response(user_input)
    st.session_state.messages.append(("bot", response))
    st.experimental_rerun()
