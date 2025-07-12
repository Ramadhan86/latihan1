# Chatbot sederhana: Pengetahuan Merakit PC/Laptop
import streamlit as st

# Pengetahuan mendetail tentang merakit PC/laptop
knowledge = [
    "Langkah pertama merakit PC adalah menentukan kebutuhan penggunaan (gaming, desain, kantor, dsb).",
    "Motherboard adalah papan utama tempat semua komponen PC terpasang.",
    "Prosesor (CPU) adalah otak komputer yang menjalankan instruksi program.",
    "Pilih motherboard yang kompatibel dengan prosesor (socket harus sama).",
    "RAM (Random Access Memory) berfungsi sebagai memori sementara saat komputer bekerja.",
    "Jumlah dan kecepatan RAM mempengaruhi performa multitasking.",
    "Pilih power supply (PSU) dengan daya yang cukup dan bersertifikat (misal 80+ Bronze).",
    "SSD lebih cepat dari HDD dan mempercepat booting serta loading aplikasi.",
    "VGA/Graphics Card diperlukan untuk gaming atau desain grafis berat.",
    "Pastikan casing cukup besar untuk menampung semua komponen dan memiliki ventilasi baik.",
    "Gunakan thermal paste di antara CPU dan heatsink untuk mencegah overheat.",
    "Pasang RAM pada slot yang sesuai (perhatikan dual channel).",
    "Motherboard biasanya memiliki port SATA untuk HDD/SSD dan M.2 untuk NVMe SSD.",
    "Pastikan semua kabel power (24-pin, 8-pin CPU, VGA) terpasang dengan benar.",
    "Gunakan standoff saat memasang motherboard ke casing agar tidak terjadi short."
    "Perhatikan arah kipas casing: intake (masuk) dan exhaust (keluar) untuk sirkulasi udara.",
    "Sebelum merakit, pastikan Anda sudah membuang listrik statis dari tubuh (grounding).",
    "Baca manual motherboard untuk mengetahui posisi pin power, reset, dan LED.",
    "Pasang prosesor dengan hati-hati, jangan menekan terlalu keras agar pin tidak bengkok.",
    "Gunakan obeng magnetik agar baut tidak mudah jatuh ke dalam casing.",
    "Setelah semua terpasang, cek kembali semua konektor dan baut sebelum menyalakan PC.",
    "Install sistem operasi (Windows, Linux, dsb) setelah perakitan selesai.",
    "Update BIOS/UEFI jika diperlukan untuk mendukung hardware terbaru.",
    "Pastikan driver hardware (VGA, LAN, Audio) terinstal dengan benar.",
    "Gunakan cable management agar aliran udara di dalam casing tetap baik.",
    "Jika menggunakan dua storage (SSD+HDD), install OS di SSD untuk performa maksimal.",
    "Perhatikan wattage total komponen saat memilih PSU.",
    "Monitor dengan refresh rate tinggi cocok untuk gaming.",
    "Laptop umumnya tidak bisa di-upgrade CPU dan VGA, hanya RAM dan storage.",
    "Gunakan thermal pad atau cooling pad untuk laptop agar suhu tetap stabil.",
    "Jangan lupa memasang I/O shield pada casing sebelum motherboard.",
    "Periksa kompatibilitas ukuran motherboard (ATX, mATX, ITX) dengan casing.",
    "Gunakan anti-virus setelah instalasi OS untuk keamanan data.",
    "Backup data penting sebelum melakukan upgrade hardware.",
    "Overclocking dapat meningkatkan performa, tapi perhatikan suhu dan garansi.",
    "Pilih monitor dengan resolusi sesuai kebutuhan (Full HD, 2K, 4K).",
    "Gunakan UPS untuk melindungi PC dari mati listrik mendadak.",
    "Pilih keyboard dan mouse sesuai ergonomi agar nyaman digunakan lama.",
    "Jangan menyalakan PC tanpa pendingin CPU terpasang.",
    "Periksa garansi setiap komponen sebelum membeli."
]

def get_response(user_input):
    user_input = user_input.lower()
    if "cpu" in user_input or "prosesor" in user_input:
        return "CPU adalah otak komputer. Pastikan memilih prosesor dan motherboard yang kompatibel (socket sama)."
    elif "motherboard" in user_input:
        return "Motherboard adalah papan utama. Perhatikan ukuran (ATX, mATX, ITX) dan kompatibilitas dengan komponen lain."
    elif "ram" in user_input:
        return "RAM berfungsi sebagai memori sementara. Pilih jumlah dan kecepatan sesuai kebutuhan."
    elif "psu" in user_input or "power supply" in user_input:
        return "Pilih PSU dengan daya cukup dan sertifikasi minimal 80+ Bronze."
    elif "vga" in user_input or "graphics" in user_input:
        return "VGA/Graphics Card penting untuk gaming dan desain grafis. Pastikan kompatibel dengan motherboard dan PSU."
    elif "ssd" in user_input or "hdd" in user_input or "storage" in user_input:
        return "SSD lebih cepat dari HDD. Install OS di SSD untuk performa maksimal."
    elif "casing" in user_input:
        return "Pilih casing yang cukup besar dan memiliki ventilasi baik."
    elif "thermal" in user_input:
        return "Gunakan thermal paste di antara CPU dan heatsink untuk mencegah overheat."
    elif "kipas" in user_input or "fan" in user_input:
        return "Atur arah kipas: intake (masuk) dan exhaust (keluar) untuk sirkulasi udara."
    elif "grounding" in user_input or "statis" in user_input:
        return "Lakukan grounding sebelum merakit untuk mencegah kerusakan akibat listrik statis."
    elif "bios" in user_input or "uefi" in user_input:
        return "Update BIOS/UEFI jika diperlukan agar mendukung hardware terbaru."
    elif "driver" in user_input:
        return "Pastikan semua driver hardware terinstal setelah OS diinstall."
    elif "cable" in user_input:
        return "Lakukan cable management agar aliran udara tetap baik dan rapi."
    elif "os" in user_input or "sistem operasi" in user_input:
        return "Install OS (Windows, Linux, dsb) setelah perakitan selesai."
    elif "monitor" in user_input:
        return "Pilih monitor dengan refresh rate dan resolusi sesuai kebutuhan."
    elif "laptop" in user_input:
        return "Pada laptop, umumnya hanya RAM dan storage yang bisa di-upgrade."
    elif "overclock" in user_input:
        return "Overclocking dapat meningkatkan performa, tapi perhatikan suhu dan garansi."
    elif "usb" in user_input or "i/o" in user_input:
        return "Jangan lupa memasang I/O shield sebelum motherboard ke casing."
    elif "backup" in user_input:
        return "Selalu backup data penting sebelum upgrade hardware."
    elif "garansi" in user_input:
        return "Periksa garansi setiap komponen sebelum membeli."
    elif "cooling" in user_input or "pad" in user_input:
        return "Gunakan cooling pad untuk laptop agar suhu tetap stabil."
    elif "keyboard" in user_input or "mouse" in user_input:
        return "Pilih keyboard dan mouse yang ergonomis agar nyaman digunakan."
    elif "ups" in user_input:
        return "Gunakan UPS untuk melindungi PC dari mati listrik mendadak."
    elif "manual" in user_input:
        return "Baca manual motherboard untuk mengetahui posisi pin power, reset, dan LED."
    elif "baut" in user_input or "obeng" in user_input:
        return "Gunakan obeng magnetik agar baut tidak mudah jatuh ke dalam casing."
    elif "standoff" in user_input:
        return "Gunakan standoff saat memasang motherboard agar tidak terjadi short."
    elif "ventilasi" in user_input:
        return "Pastikan casing memiliki ventilasi yang baik untuk sirkulasi udara."
    elif "install" in user_input:
        return "Setelah perakitan, install OS dan driver hardware."
    else:
        import random
        return random.choice(knowledge)

st.title("Chatbot Merakit PC/Laptop 🖥️💻")
st.write("Tanyakan apa saja seputar merakit PC atau laptop. Chatbot ini berisi pengetahuan mendetail untuk membantu Anda!")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Anda:")
if st.button("Kirim") or user_input:
    if user_input:
        response = get_response(user_input)
        st.session_state['chat_history'].append((user_input, response))

for i, (q, a) in enumerate(st.session_state['chat_history']):
    st.markdown(f"**Anda:** {q}")
    st.markdown(f"**Chatbot:** {a}")
