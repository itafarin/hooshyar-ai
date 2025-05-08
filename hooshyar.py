import streamlit as st
import openai
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="هوش‌یار | مشاور تحصیلی هوشمند", page_icon="🎓")

st.title("🎓 هوش‌یار")
st.markdown("👋 به مشاور هوشمند تحصیلی خوش آمدید. سوال خود را بپرسید:")

question = st.text_input("سوال:")

if question:
    with st.spinner("در حال پردازش..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "شما یک مشاور تحصیلی هوشمند هستید که به دانش‌آموزان کمک می‌کنید رشته مناسب انتخاب کنند."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.success("✅ پاسخ:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ خطا در دریافت پاسخ: {str(e)}")
