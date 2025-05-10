import streamlit as st
import google.generativeai as genai

# --- تنظیمات API ---
try:
    API_KEY = st.secrets["gemini"]["api_key"]
except:
    st.error("❌ کلید API یافت نشد.")
    st.stop()

genai.configure(api_key=API_KEY)

# --- بارگذاری مدل Gemini ---
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"❌ مدل Gemini قابل دسترسی نیست: {e}")
    st.stop()

# --- استایل و عنوان ---
st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")

st.markdown("""
    <style>
        body > div > div > div > div > div {
            direction: rtl;
            text-align: right;
            font-family: 'Tahoma', 'Nafees', sans-serif;
        }
        .message {
            padding: 10px;
            margin: 8px 0;
            border-radius: 8px;
            background-color: #f0f0f0;
        }
        .user {
            background-color: #DCF8C6;
            text-align: right;
        }
        .bot {
            background-color: #ECECEC;
            text-align: right;
        }
        .stTextInput textarea {
            height: 120px;
            font-size: 16px;
        }
        .stButton button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 هوش‌یار")
st.markdown("👋 سلام! من هوش‌یار هستم — مشاور تحصیلی هوشمند دانشگاه ملی مهارت. سوال خود را بپرسید:")

# --- session_state ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_input_value" not in st.session_state:
    st.session_state.user_input_value =
