import streamlit as st
import requests

HF_API_KEY = "hf_..."  # ← کلید HuggingFace خود را اینجا قرار بده

st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")
st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

question = st.text_input("سوال:")

def ask_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {
        "inputs": f"""شما یک مشاور تحصیلی هستید. سوال کاربر: {prompt}""",
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["generated_text"]

if question:
    with st.spinner("در حال پردازش..."):
        try:
            result = ask_huggingface(question)
            st.success("✅ پاسخ:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ خطا: {e}")
