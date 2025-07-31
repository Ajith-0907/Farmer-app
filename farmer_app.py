import streamlit as st
from streamlit.components.v1 import html

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
        "response": "స్థానిక వాతావరణాన్ని గమనించండి. కరువు కోసం డ్రిప్ ఇరిగేషన్ వాడండి; చలికాలం నివారణకు షీట్లు లేదా స్ప్రింక్‌లర్ వాడండి."
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

# Function to generate response
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

# Injecting custom HTML UI
custom_ui = """
    <div class="container" style="font-family: 'Segoe UI'; max-width: 800px; margin: auto;">
        <h1 style="text-align: center; color: #2e7d32;">రైతు సహాయక చాట్‌బాట్</h1>
        <div id="chat-box" style="background-color: white; border-radius: 10px; padding: 20px; height: 500px; overflow-y: scroll; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);"></div>
        <div style="display: flex; margin-top: 10px;">
            <input id="user-input" type="text" placeholder="మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి..." style="flex: 1; padding: 10px; border-radius: 20px; border: 1px solid #ccc;" onkeydown="if(event.key === 'Enter'){sendMessage()}"/>
            <button onclick="sendMessage()" style="margin-left: 10px; padding: 10px 20px; border-radius: 20px; background-color: #4caf50; color: white; border: none;">పంపించండి</button>
        </div>
    </div>

    <script>
        function sendMessage() {
            var input = document.getElementById('user-input');
            var message = input.value.trim();
            if (message === '') return;
            var chatBox = document.getElementById('chat-box');
            chatBox.innerHTML += `<div style='text-align: right; margin: 10px;'><span style='background-color: #e3f2fd; padding: 10px 15px; border-radius: 18px; display: inline-block;'>${message}</span></div>`;
            fetch('/chatbot', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({message: message})})
                .then(response => response.json())
                .then(data => {
                    chatBox.innerHTML += `<div style='text-align: left; margin: 10px;'><span style='background-color: #f1f1f1; padding: 10px 15px; border-radius: 18px; display: inline-block;'>${data.response}</span></div>`;
                    chatBox.scrollTop = chatBox.scrollHeight;
                });
            input.value = '';
        }
    </script>
"""

# Handle Streamlit POST route
from streamlit_javascript import st_javascript
import json

query = st_javascript("""
    if (!window.responseBuffer) {
        window.responseBuffer = [];
        const originalFetch = window.fetch;
        window.fetch = function() {
            const args = arguments;
            if (args[0] === '/chatbot') {
                return new Promise(resolve => {
                    const reader = new Response(JSON.stringify({response: window.lastResponse || 'లోపం. ప్రయత్నించండి.'})).body.getReader();
                    resolve(new Response(reader.read().then(({value}) => new Uint8Array(value))));
                });
            }
            return originalFetch.apply(this, args);
        }
    }
    """)

# Display custom HTML UI
tmp = html(custom_ui, height=700)

# Receive user input via Streamlit's chat API
if st.query_params.get("message"):
    msg = st.query_params.get("message")
    st.write(json.dumps({"response": get_response(msg)}))
