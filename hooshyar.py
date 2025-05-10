import streamlit as st
import google.generativeai as genai

# دریافت کلید API از فایل secrets
API_KEY = st.secrets["gemini"]["api_key"]

# پیکربندی کتابخانه genai با کلید API شما
genai.configure(api_key=API_KEY)

# انتخاب مدل Gemini Pro (تلاش با نام فعلی احتمالی)
model = genai.GenerativeModel('gemini-1.5-pro')

# تنظیمات صفحه
st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")
st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

# دریافت سوال از کاربر
question = st.text_input("سوال:")

# تابع پرسش از مدل Gemini
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"خطا در مدل Gemini: {e}")

# وقتی کاربر سوالی وارد کند
if question:
    with st.spinner("در حال پردازش..."):
        try:
            prompt = f"سوال مشاوره تحصیلی: {question}"
            result = ask_gemini(prompt)
            st.success("✅ پاسخ:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ خطا: {e}")
