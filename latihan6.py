# Chatbot Streamlit dengan API Gemini, context file (txt, pdf, excel)
import streamlit as st
import os
import pandas as pd
import PyPDF2

# --- Konfigurasi Gemini API ---
import requests
GEMINI_API_KEY = st.secrets["AIzaSyCWPG3vt4Pie-sA6YsFZ7-_npujetrehV0"] if "AIzaSyCWPG3vt4Pie-sA6YsFZ7-_npujetrehV0" in st.secrets else "AIzaSyCWPG3vt4Pie-sA6YsFZ7-_npujetrehV0"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

def extract_text_from_file(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[-1].lower()
    if ext == ".txt":
        return uploaded_file.read().decode("utf-8")
    elif ext == ".pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(uploaded_file)
        return df.to_string(index=False)
    else:
        return "Format file tidak didukung. Hanya .txt, .pdf, .xls, .xlsx."

def gemini_chat(context, user_input):
    prompt = f"Jawablah pertanyaan berikut hanya berdasarkan informasi yang ada di context. Jika tidak ada di context, jawab 'Maaf, saya tidak menemukan informasi tersebut di file.'\n\nContext:\n{context}\n\nPertanyaan: {user_input}\nJawaban:"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 256}
    }
    response = requests.post(GEMINI_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        try:
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception:
            return "Maaf, terjadi kesalahan pada respons API."
    else:
        return f"Gagal menghubungi API Gemini: {response.text}"

st.title("Chatbot Gemini Berbasis Context File")
st.write("Upload file (.txt, .pdf, .xls, .xlsx) sebagai context. Chatbot hanya akan menjawab berdasarkan isi file tersebut.")

uploaded_file = st.file_uploader("Upload file context", type=["txt", "pdf", "xls", "xlsx"])

if uploaded_file:
    context = extract_text_from_file(uploaded_file)
    st.text_area("Isi context (ringkasan)", context[:2000], height=200)
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []
    user_input = st.text_input("Anda:")
    if st.button("Kirim") or user_input:
        if user_input:
            answer = gemini_chat(context, user_input)
            st.session_state['chat_history'].append((user_input, answer))
    for q, a in st.session_state['chat_history']:
        st.markdown(f"**Anda:** {q}")
        st.markdown(f"**Chatbot:** {a}")
else:
    st.info("Silakan upload file context terlebih dahulu.")
