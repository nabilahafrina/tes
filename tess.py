import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Pengenalan Risiko Kimia", layout="wide")

# Judul halaman
st.title("🧪 Pengenalan Risiko dan Cara Menangani Senyawa Kimia")
st.markdown("---")

# Pendahuluan
st.header("📘 Pendahuluan")
st.write("""
Senyawa kimia digunakan dalam berbagai kegiatan laboratorium dan industri. 
Namun, senyawa ini juga memiliki risiko yang dapat membahayakan keselamatan dan kesehatan jika tidak ditangani dengan benar. 
Penting bagi siapa pun yang bekerja dengan bahan kimia untuk memahami risikonya dan cara penanganan yang aman.
""")

# Jenis risiko kimia
st.header("⚠️ Jenis Risiko Senyawa Kimia")
st.markdown("""
- 🔥 **Mudah Terbakar**: Seperti etanol dan aseton.
- ☠️ **Beracun**: Misalnya sianida dan merkuri.
- 🧪 **Korosif**: Seperti asam sulfat atau natrium hidroksida.
- 💥 **Reaktif**: Contohnya natrium logam atau peroksida organik.
""")

# Cara menangani dengan aman
st.header("✅ Cara Menangani Senyawa Kimia dengan Aman")
st.markdown("""
1. Gunakan **APD (Alat Pelindung Diri)**: sarung tangan, kacamata, masker, dan jas lab.
2. Simpan bahan kimia sesuai prosedur yang benar dan ikuti **MSDS** (Material Safety Data Sheet).
3. Hindari mencampur bahan tanpa pemahaman reaktivitasnya.
4. Gunakan **lemari asam** untuk zat yang mudah menguap atau berbahaya.
5. Kenali simbol-simbol bahaya pada label bahan kimia.
""")

# Gambar simbol bahaya
st.header("📌 Simbol-Simbol Bahaya Kimia")
cols = st.columns(3)

with cols[0]:
    st.image("https://upload.wikimedia.org/wikipedia/commons/5/5a/GHS-pictogram-flamme.svg", caption="Mudah Terbakar", width=120)

with cols[1]:
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e6/GHS-pictogram-skull.svg", caption="Beracun", width=120)

with cols[2]:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/06/GHS-pictogram-corrosif.svg", caption="Korosif", width=120)

# Kuis sederhana
st.header("🧠 Kuis Cepat: Coba Uji Pengetahuanmu!")

question = st.radio("Simbol tengkorak pada label kimia menunjukkan bahwa zat tersebut...", (
    "Sangat korosif",
    "Mudah terbakar",
    "Beracun atau mematikan",
    "Reaktif terhadap air"
))

if st.button("Cek Jawaban"):
    if question == "Beracun atau mematikan":
        st.success("✅ Benar! Simbol tengkorak menunjukkan bahan yang beracun atau mematikan.")
    else:
        st.error("❌ Salah. Jawaban yang benar adalah: Beracun atau mematikan.")

# Penutup
st.markdown("---")
st.info("📌 Catatan: Selalu baca MSDS sebelum menangani bahan kimia dan patuhi prosedur keselamatan yang berlaku.")

