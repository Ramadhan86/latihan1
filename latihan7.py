# Chatbot Streamlit + Gemini: Hanya menjawab tentang Teknik Komputer dan Jaringan
import streamlit as st
import requests

# Informasi context tentang Teknik Komputer dan Jaringan (TKJ)
context = (
    "Jurusan Teknik Komputer dan Jaringan (TKJ) adalah salah satu jurusan di SMK yang mempelajari tentang komputer, jaringan komputer, perangkat keras, perangkat lunak, serta instalasi dan pemeliharaan jaringan. "
    "Lulusan TKJ dibekali kemampuan merakit komputer, menginstal sistem operasi, mengelola server, membuat jaringan LAN, WLAN, dan troubleshooting jaringan. "
    "Mata pelajaran utama meliputi dasar-dasar komputer, jaringan dasar, administrasi server, keamanan jaringan, dan teknologi cloud. "
    "Prospek kerja lulusan TKJ antara lain teknisi jaringan, administrator jaringan, IT support, teknisi komputer, hingga wirausaha di bidang IT. "
    "Sertifikasi yang dapat diambil antara lain MTCNA, CCNA, dan CompTIA Network+. "
    "TKJ juga mempelajari pemrograman dasar, IoT, dan perangkat jaringan seperti router, switch, dan access point. "
    "Lulusan TKJ dapat melanjutkan ke perguruan tinggi di bidang teknik informatika, sistem informasi, atau teknik komputer. "
    "Kompetensi lain yang diajarkan adalah etika profesi, komunikasi bisnis, dan kewirausahaan di bidang teknologi informasi."
)

GEMINI_API_KEY = "AIzaSyB0goOJWc6lt45Lg4a551PUchNNT0EZTKg"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

def gemini_chat(context, user_input):
    prompt = f"Jawablah pertanyaan berikut hanya berdasarkan informasi yang ada di context. Jika tidak ada di context, jawab 'Maaf, saya tidak menemukan informasi tersebut.'\n\nContext:\n{context}\n\nPertanyaan: {user_input}\nJawaban:"
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

st.title("Chatbot Gemini: Teknik Komputer dan Jaringan (TKJ)")
st.write("Tanyakan apa saja seputar jurusan Teknik Komputer dan Jaringan. Chatbot hanya akan menjawab berdasarkan informasi yang tersedia.")

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
