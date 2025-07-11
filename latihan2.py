import streamlit as st

st.title("Kalkulator Sederhana dengan Streamlit")

angka1 = st.number_input("Masukkan angka pertama:", value=0.0)
angka2 = st.number_input("Masukkan angka kedua:", value=0.0)
operasi = st.selectbox("Pilih operasi:", ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"])

hasil = None
if operasi == "Tambah (+)":
    hasil = angka1 + angka2
elif operasi == "Kurang (-)":
    hasil = angka1 - angka2
elif operasi == "Kali (×)":
    hasil = angka1 * angka2
elif operasi == "Bagi (÷)":
    if angka2 != 0:
        hasil = angka1 / angka2
    else:
        hasil = "Tidak bisa dibagi dengan nol!"