import streamlit as st

st.set_page_config(page_title="రైతు సహాయక చాట్‌బాట్", layout="centered")

# Telugu knowledge base
knowledge_base = {
    "pests": {
        "keywords": ["పెస్ట్", "పురుగులు", "ఇన్సెక్ట్", "ఇన్ఫెస్టేషన్"],
        "response": "సాధారణ పురుగుల్లో ఆఫిడ్స్, చైతూనిరుగులు, బీట్‌ల్స్ ఉంటాయి. జీవ సురక్షిత నియంత్రణకు నీమ్ ఆయిల్ లేదా పురుగుమందు సబ్బు వాడండి."
    },
    "diseases": {
        "keywords": ["వ్యాధి", "ఫంగస్", "బ్లైట్", "రాట్", "విల్టింగ్"],
        "response": "చెట్లు పొందే వ్యాధులు ఫంగల్, బ్యాక్టీరియల్ లేదా వైరల్ కావచ్చు. వ్యాధి నిరోధక రకాలు, పంట మార్పిడి, ఫంగిసైడ్లు వాడడం మంచిది."
    },
    "fertilizer": {
        "keywords": ["ఫెర్టిలైజర్", "పోషకాలు", "ఎన్‌పీకే", "మనం", "కాంపోస్ట్"],
        "response": "మట్టి పరీక్ష చేసుకోవడం ఉత్తమం. జీవ పోషకాలు కోసం కాంపోస్ట్ లేదా చెత్త వాడండి. ఎన్‌పీకే 10-10-10 లాంటి సంతులిత ఎరువులు ఉపయోగించండి."
    },
    "weather": {
        "keywords": ["వాతావరణం", "వర్షం", "కరువు", "చలికాలం"],
        "response": "స్థానిక వాతావరణాన్ని గమనించండి. కరువు కోసం డ్రిప్ ఇరిగేషన్ వాడండి; చలికాలం నివారణకు షీట్లు లేదా స్ప్రింక్లర్ వాడండి."
    },
    "crop selection": {
        "keywords": ["పంట", "విత్తనాలు", "ఎంపిక", "కృషి"],
        "response": "మట్టి, వాతావరణం మరియు మార్కెట్ డిమాండ్ ఆధారంగా పంటలు ఎంచుకోండి."
    },
    "irrigation": {
        "keywords": ["నీరు", "ఇరిగేషన్", "డ్రిప్", "స్ప్రింక్లర్"],
        "response": "డ్రిప్ లేదా స్ప్రింక్లర్ వాడటం ఉత్తమం. మట్టి తేమను పరిశీలిస్తూ నీరు సమర్థవంతంగా వాడండి."
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

# Display previous messages
for msg in st.session_state.messages:
    role, text = msg
    with st.chat_message(role):
        st.markdown(text)

# Chat input
user_input = st.chat_input("మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(("user", user_input))

    # Get bot response
    response = get_response(user_input)
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append(("assistant", response))
