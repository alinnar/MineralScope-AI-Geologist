import streamlit as st
import os
from PIL import Image

def show_home():

    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../resources/style/style.css")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)
    st.markdown("""
                <div class='header'><h1>Selamat Datang di MineralScope: AI Geologist!💎⛏️</h1></div>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class='section'>
        <div class='header'><h2>Apa itu Mineral?</h2></div>
        <div class='font'>
            <p><strong>Mineral</strong> adalah bahan alami yang terbentuk secara geologis dalam bumi. Mineral terdiri dari unsur-unsur kimia tertentu yang memiliki struktur kristal yang teratur. 
            Mereka adalah bahan dasar pembentuk batuan dan memiliki berbagai macam sifat fisik seperti warna, kekerasan, dan kilau. 
            Beberapa contoh mineral yang terkenal termasuk quartz, mika, dan pyrite.
            Mineral sangat penting dalam berbagai aspek kehidupan, mulai dari industri pertambangan, pembuatan peralatan, hingga penelitian geologi. Oleh karena itu, pengenalan dan pemahaman tentang jenis-jenis mineral sangat penting dalam dunia ilmiah dan industri.</p> 
        </div>
    </div> 
                """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Kenapa Klasifikasi Mineral Itu Penting?</h2></div>
            <div class='font'>
                <p>Klasifikasi mineral membantu dalam mengelompokkan berbagai jenis mineral berdasarkan karakteristik fisik dan kimia mereka. Proses ini sangat penting dalam penelitian geologi untuk mengetahui asal-usul, penyebaran, dan potensi penggunaan mineral dalam industri.
                Selain itu, klasifikasi mineral juga membantu para geolog, ilmuwan, dan industri dalam mencari dan memanfaatkan sumber daya alam secara lebih efektif dan efisien. Dengan klasifikasi yang tepat, kita dapat menentukan penggunaan mineral yang lebih optimal, seperti dalam pembuatan barang-barang elektronik, konstruksi, dan energi.
                </p>
            </div>    
        </div>
                """, unsafe_allow_html=True)

    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Fitur Utama Aplikasi</h2></div>
            <div class='font'>
                <p>\n<strong>💎Deteksi Mineral:</strong> Fitur ini membantu pengguna untuk mengidentifikasi jenis mineral dengan cara unggah gambar atau ambil gambar.
                    Aplikasi ini akan mengindentifikasi apakah mineral anda termasuk kedalam jenis <strong>Biotite, Bornite, Chrysocolla, Malachite, Muscovite, Pyrite, atau Quartz</strong>.
                \n<strong>🧾Informasi Mineral:</strong> Setelah Mendeteksi mineral, aplikasi akan memberikan penjelasan singkat tentang mineral yang terdeteksi.
                \n<strong>🗺️Peta Persebaran Mineral di Indonesia:</strong> Menampilkan lokasi geografis di Indonesia di mana mineral tertentu ditemukan. Fitur ini memungkinkan pengguna untuk memahami persebaran mineral secara visual melalui peta interaktif.</p>
            </div>    
        </div>
                """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='section'>
            <div class='header'><h2>Cara Penggunaan Aplikasi</h2></div>
            <div class='font'>
                <p>
                Untuk mendeteksi mineral, buka menu Analyze:
                \n1. Pilih opsi "Upload Foto" atau "Ambil Foto"
                \n2. Unggah atau ambil gambar mineral.
                \n3. Klik tombol "Analisis Gambar" untuk melihat hasil klasifikasi dan informasi detail mineral.</p>
                """, unsafe_allow_html=True)