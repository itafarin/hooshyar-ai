import streamlit as st
import requests

# دریافت کلید API از secrets (در فایل .streamlit/secrets.toml)
HF_API_KEY = st.secrets["hf"]["api_key"]

# تنظیمات صفحه
st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")
st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

# ورودی کاربر
question = st.text_input("سوال:")

def ask_huggingface(prompt):
    # استفاده از مدل Falcon-RW-1B به جای Mistral
    # API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-rw-1b"
    API_URL = "https://api-inference.huggingface.co/models/gpt2 "

    
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }
    
    payload = {
        "inputs": f"[INST] شما یک مشاور تحصیلی هستید. سوال کاربر: {prompt} [/INST]",
        "parameters": {
            "max_new_tokens": 200,     # حداکثر تعداد کلمات تولیدی
            "temperature": 0.8,        # خلاقیت مدل
            "do_sample": True          # اجازه دادن به مدل برای پاسخ‌های متنوع
        },
        "options": {
            "wait_for_model": True,    # منتظر شدن برای استارت مدل
            "use_cache": False         # غیرفعال کردن کش برای پاسخ‌های جدید
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0].get("generated_text", "پاسخی دریافت نشد.")
    else:
        raise Exception(f"خطا در API: {response.status_code} - {response.text}")

# اجرای پرسش و نمایش پاسخ
if question:
    with st.spinner("در حال پردازش..."):
        try:
            result = ask_huggingface(question)
            st.success("✅ پاسخ:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ خطا: {e}")
