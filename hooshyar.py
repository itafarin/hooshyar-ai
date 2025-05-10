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

# عنوان و متن خوش‌آمدگویی
st.title("🎓 هوش‌یار")
st.markdown("👋 سلام! به مشاور هوشمند تحصیلی دانشگاه ملی مهارت خوش آمدید. سوال خود را بپرسید:")

# دریافت سوال از کاربر
question = st.text_area("سوال:", placeholder="مثلاً: بهترین رشته برای کنکور چیست؟")

# تابع پرسش از مدل Gemini
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"خطا در مدل Gemini: {e}")

# دکمه "بپرس"
if st.button("🔍 بپرس"):
    if question.strip() == "":
        st.warning("⚠️ لطفاً یک سوال وارد کنید.")
    else:
        with st.spinner("در حال پردازش..."):
            try:
                prompt = f"سوال مشاوره تحصیلی: {question}"
                result = ask_gemini(prompt)
                st.success("✅ پاسخ:")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ خطا: {e}")
