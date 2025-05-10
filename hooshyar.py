import streamlit as st
import google.generativeai as genai

# دریافت کلید API از فایل secrets
API_KEY = st.secrets["gemini"]["api_key"]

# پیکربندی کتابخانه genai با کلید API شما
genai.configure(api_key=API_KEY)

# انتخاب مدل Gemini Flash (در صورت دسترسی)
model = genai.GenerativeModel('gemini-1.5-flash')

# تنظیمات صفحه
st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")

# استایل برای راست چین کردن محتوا و فونت فارسی
st.markdown("""
    <style>
        body > div > div > div > div > div {
            direction: rtl;
            text-align: right;
            font-family: 'Tahoma', 'Nafees', 'Arial', sans-serif;
        }
        .message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 8px;
            line-height: 1.6em;
        }
        .user-message {
            background-color: #DCF8C6;
            text-align: right;
        }
        .bot-message {
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

# عنوان و معرفی
st.title("🎓 هوش‌یار")
st.markdown("👋 سلام! من هوش‌یار هستم — مشاور تحصیلی هوشمند دانشگاه ملی مهارت. سوال خود را بپرسید:")

# ایجاد session_state برای ذخیره تاریخچه چت
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# دریافت سوال از کاربر
user_input = st.text_area("سوال:", placeholder="مثلاً: بهترین رشته برای کنکور چیست؟", key="input_area")

col1, col2 = st.columns([3, 1])
with col1:
    send_button = st.button("🔍 بپرس")
with col2:
    clear_button = st.button("🗑️ پاک کردن چت")

# عملیات پاک کردن چت
if clear_button:
    st.session_state.chat_history = []
    st.experimental_rerun()

# وقتی کاربر سوالی وارد کند
if send_button and user_input.strip() != "":
    # افزودن سوال کاربر به تاریخچه
    st.session_state.chat_history.append(("user", user_input))

    with st.spinner("در حال پردازش..."):
        try:
            response = model.generate_content(user_input)
            bot_response = response.text
            # افزودن پاسخ هوش مصنوعی به تاریخچه
            st.session_state.chat_history.append(("bot", bot_response))
        except Exception as e:
            st.session_state.chat_history.append(("bot", f"❌ خطایی رخ داد: {e}"))

        # پاک کردن کادر ورودی بعد از ارسال
        st.session_state.input_area = ""

# نمایش تاریخچه چت
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f'<div class="message user-message">🧑‍💻 شما: {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message">🤖 هوش‌یار: {message}</div>', unsafe_allow_html=True)
