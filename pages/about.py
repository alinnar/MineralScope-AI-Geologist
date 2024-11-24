import streamlit as st
import os
from PIL import Image


def show_about():
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
            <div class='header'><h1>🧾Tentang</h1></div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class='section'>
                <div class='header'><h2>Apa itu MineralScope?</h2></div>
                <div class='font'>
                    <p><strong>MineralScope</strong> adalah aplikasi berbasis teknologi kecerdasan buatan (AI) yang memanfaatkan model Convolutional Neural Network (CNN) untuk melakukan klasifikasi gambar mineral secara cepat dan akurat.
                    Aplikasi ini dirancang untuk membantu pengguna, mulai dari pelajar hingga peneliti geologi, dalam mengenali jenis-jenis mineral melalui gambar yang diunggah atau diambil langsung. Selain itu, aplikasi ini juga memberikan informasi tentang mineral yang terdeteksi.
                    Aplikasi ini juga menyediakan gambaran persebaran mineral yang ada di Indonesia.
                    </p> 
                </div>
            </div> 
                        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div class='section'>
                <div class='header'><h2>Keterbatasan Aplikasi</h2></div>
                <div class='font'>
                    <p>
                    \n1. <strong>Ketergantungan pada Kualitas Gambar:</strong> Akurasi deteksi mineral sangat bergantung pada kualitas gambar yang diunggah atau diambil. Gambar buram, terlalu gelap, atau memiliki sudut pandang yang tidak tepat dapat memengaruhi hasil analisis.
                    \n2. <strong>Jumlah Mineral yang Diklasfifikasi:</strong> Aplikasi hanya mampu mengenali jenis mineral yang sudah dilatih dalam model. Mineral yang tidak termasuk dalam dataset pelatihan tidak akan terdeteksi atau mungkin terklasifikasi secara keliru.
                    \n3. <strong>Kemiripan Antar-Mineral:</strong> Mineral dengan sifat fisik atau penampilan visual yang mirip dapat menyebabkan model bingung, sehingga menghasilkan prediksi dengan akurasi yang lebih rendah.
                    \n4. <strong>Keterbatasan Peta Persebaran:</strong> Peta persebaran mineral hanya pada beberapa wilayah di Indonesia.
                    </p> 
                </div>
            </div> 
                        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='section'>
            <div class='header'><h2>Pengembang</h2></div>
            <div class='subheader2'><h3> Revalin Arianti Rajagukguk - 22537144009 </h3></div>
            <div class="icon-container">
                <a href="https://github.com/alinnar" target="_blank" class="social-icon github" aria-label="Github"></a>
                <a href="https://www.instagram.com/alinnrar?igsh=ZHF6bXQ4M3BzbGwx" target="_blank" class="social-icon instagram" aria-label="Instagram"></a>
                <a href="mailto:revalinarianti.2022@student.uny.ac.id" class="social-icon email" aria-label="Email"></a>
            </div>
        </div>
        """, unsafe_allow_html=True)

        