import streamlit as st
import requests

# دریافت کلید از فایل secrets
HF_API_KEY = st.secrets["hf"]["api_key"]

# تنظیمات صفحه
st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")
st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

# دریافت سوال از کاربر
question = st.text_input("سوال:")

# تابع پرسش از مدل HuggingFace
def ask_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 128},
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        raise Exception(f"خطا در API: {response.status_code} - {response.text}")

# وقتی کاربر سوالی وارد کند
if question:
    with st.spinner("در حال پردازش..."):
        try:
            prompt = f"سوال مشاوره تحصیلی: {question}\nپاسخ:"
            result = ask_huggingface(prompt)
            st.success("✅ پاسخ:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ خطا: {e}")
