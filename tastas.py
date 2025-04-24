import streamlit as st
import ollama

client = ollama.Client()

# Set page config with centered layout and emoji title
st.set_page_config(page_title="💬 Fashion ChatBot", layout="centered")
st.title("💄✨ Tastas - Xclusive Fashion Chatbot")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "skin_tone" not in st.session_state:
    st.session_state.skin_tone = None
if "body_type" not in st.session_state:
    st.session_state.body_type = "athletic"  # Start with athletic

# Helper to cycle body type
def cycle_body_type(current):
    order = ["athletic", "medium", "fat"]
    next_index = (order.index(current) + 1) % len(order)
    return order[next_index]

# Sidebar inputs for skin tone selection
with st.sidebar:
    st.header("Your Profile")
    skin_tone = st.selectbox(
        "Select your skin tone:",
        options=["Fair", "Medium", "Olive", "Brown", "Dark"],
        index=2 if st.session_state.skin_tone is None else
              ["Fair", "Medium", "Olive", "Brown", "Dark"].index(st.session_state.skin_tone)
    )
    st.session_state.skin_tone = skin_tone

# Bot response function with added skin tone and body type context
def bot_response(user_input, context_dict, skin_tone, body_type):
    task = (
        "<Task starts> You are a professional Fashion Consultant Bot, specializing in personalized fashion and hairstyle suggestions. "
        "Based on the user's face shape, size, skin tone, body type, and preferences, you offer recommendations for outfits, accessories, and hairstyles that would suit them best. "
        "You focus on providing stylish, trendy, and flattering options aligned with current fashion trends while considering the user's unique features. "
        "Your responses are polite, professional, encouraging, and up to about 5 lines (~80 words). "
        "Greet back for greetings and suggest what to ask next. "
        "<Task ends> "
        "Based on the following conversation history, maintain context while generating the response for this user message. <user message starts> "
    )
    context = " <user message ends> The conversation history is provided as a dictionary below "
    context += "<context dictionary starts> " + str(context_dict) + " <context dictionary ends> "
    context += f"User skin tone: {skin_tone}. User body type: {body_type}. "
    context += (
        "<Strict Rule> Output max length ~80 words or 5 lines. Validate this <strict rule>"
        "<output format starts> Provide a concise, relevant, engaging response with interactive emojis. "
        "<output format ends> "
    )
    prompt = task + user_input + context

    response = client.generate(model="phi4-mini", prompt=prompt)
    return response['response']

# Chat input and message processing
prompt = st.chat_input("Type your fashion SOS here...")

if prompt:
    st.session_state.messages.append({'role': "user", 'content': prompt})
    st.session_state.body_type = cycle_body_type(st.session_state.body_type)

    with st.spinner("✨ Your fashion insights are being curated... 💅"):
        response = bot_response(
            prompt,
            st.session_state.messages,
            st.session_state.skin_tone,
            st.session_state.body_type
        )
        st.session_state.messages.append({'role': "assistant", 'content': response})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f"🧍‍♀️ {msg['content']}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"🛍️ {msg['content']}")