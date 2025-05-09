import streamlit as st
import requests

# دریافت کلید API از فایل secrets (بجای قرار دادن مستقیم در کد)
HF_API_KEY = st.secrets["hf"]["api_key"]

st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")
st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

question = st.text_input("سوال:")

def ask_huggingface(prompt):
    API_URL = "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": f"""شما یک مشاور تحصیلی هستید. سوال کاربر: {prompt}""",
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)

    # بررسی موفقیت پاسخ
    if response.status_code == 200:
        result = response.json()
        return result[0]["generated_text"]
    else:
        raise Exception(f"خطا در API: {response.status_code} - {response.text}")

if question:
    with st.spinner("در حال پردازش..."):
        try:
            result = ask_huggingface(question)
            st.success("✅ پاسخ:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ خطا: {e}")
