import streamlit as st
import os
import folium
from streamlit_folium import folium_static

def show_map():

    def load_css(file_path):
        with open(file_path) as f:
            st.html(f"<style>{f.read()}</style>")

    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))

    # Memuat CSS
    css_path = os.path.join(parent_dir, "../resources/style/style.css")

    # Panggil fungsi untuk memuat CSS
    load_css(css_path)
    
    def create_map():
        data = {
            'Mineral': ['Bornite', 'Bornite', 'Bornite', 'Bornite', 'Bornite', 
                        'Biotite', 'Biotite', 'Biotite', 'Biotite', 'Biotite', 
                        'Chrysocolla', 'Chrysocolla', 'Chrysocolla', 'Chrysocolla', 'Chrysocolla',
                        'Malachite', 'Malachite', 'Malachite', 'Malachite', 'Malachite',
                        'Muscovite', 'Muscovite', 'Muscovite', 'Muscovite', 'Muscovite',
                        'Pyrite', 'Pyrite', 'Pyrite', 'Pyrite', 'Pyrite',
                        'Quartz', 'Quartz', 'Quartz', 'Quartz', 'Quartz',
                        ],
            'Latitude': [0.51667,-3.55000,-3.0000, -0.51667, -4.06674, 
                         0.85651, -8.96694, 1.14562, 0.83333, -0.86104, 
                        -0.51667, -8.58102, -8.96567, -3.68, -8.60000, 
                         5.01200, -7.78333, -2.75000, 0.95194, -8.53614,
                         0.0000, -2.35636, -7.0000, -8.96694, -2.76667,
                         -4.05602, -3.0000, 0.0000, -7.31878, -6.692,
                         -4.08206, 0.17278, -3.50000, -8.06225, 3.48537,
                        ],
            'Longitude': [123.21667, 115.08306, 102.0000, 127.58333, 137.10734, 
                          99.56239, 117.38000, 127.70501, 109.25000, 119.93174, 
                          127.58333, 114.01611, 116.86724, 128.17, 118.76667, 
                          95.60300, 110.86667, 102.71667, 121.77056, 118.83446,
                          115.0000, 136.34033, 110.0000, 117.38000, 108.23333,
                          137.11320, 116.0000, 117.0000, 107.73164, 106.524,
                          137.13260, 100.81556, 114.85000, 114.24624, 125.64179,
                          ],
            'color':['blue', 'blue', 'blue', 'blue', 'blue',
                     'black', 'black', 'black', 'black', 'black',
                     'red', 'red', 'red', 'red', 'red',
                     'green', 'green', 'green', 'green', 'green',
                     'purple', 'purple', 'purple', 'purple', 'purple',
                     'orange', 'orange', 'orange', 'orange', 'orange',
                     'pink', 'pink', 'pink', 'pink', 'pink']
        }

        peta_mineral = folium.Map(location=[-2.5, 117.5], zoom_start=5)

        for mineral, lat, lon, color in zip(data['Mineral'], data['Latitude'], data['Longitude'], data['color']):
            folium.Marker(location=[lat, lon], 
                          popup=f"{mineral}",
                          icon=folium.Icon(color=color, icon='info-sign')
                          ).add_to(peta_mineral)
        return peta_mineral
    
    st.markdown("""
            <div class='header'><h1>🗺️ Peta Penyebaran Mineral di Indonesia</h1></div>
            """, unsafe_allow_html=True)

    folium_static(create_map())

    # Data detail lokasi mineral
    mineral_locations = {
        "Bornite": [
            "Sungai Kalaan, Pegunungan Meratus, Provinsi Kalimantan Selatan, Indonesia",
            "Deposit tembaga (Cu) Tapadaa, Provinsi Gorontalo, Indonesia",
            "Tambang Lebong Donok, Kabupaten Rejang Lebong, Provinsi Bengkulu, Indonesia",
            "Tambang Kaputusan, Pulau Bacan, Provinsi Maluku, Indonesia",
            "Kucing Liar, Distrik Gunung Bijih (Distrik Grasberg), Kabupaten Mimika, Provinsi Papua, Indonesia",
        ],
        "Biotite": [
            "Panyabungan, Kabupaten Mandailing Natal, Provinsi Sumatra Utara, Indonesia",
            "Deposit porfiri tembaga-emas (Cu-Au) Elang, Kabupaten Sumbawa Barat, Pulau Sumbawa, Provinsi Nusa Tenggara Barat, Indonesia",
            "Gosowong Goldfield, Pulau Halmahera, Provinsi Maluku Utara, Indonesia",
            "Prospek Ibu, Provinsi Kalimantan Barat, Indonesia",
            "Tambang Emas Poboya, Talau, Provinsi Sulawesi Tengah, Indonesia",
        ],
        "Chrysocolla": [
            "Tambang Kaputusan, Pulau Bacan, Provinsi Maluku, Indonesia",
            "Proyek Tujuh Bukit (Proyek Tumpangpitu), Provinsi Jawa Timur, Indonesia",
            "Tambang Batu Hijau, Kabupaten Sumbawa Barat, Pulau Sumbawa, Provinsi Nusa Tenggara Barat, Indonesia",
            "Maluku, Sulawesi Utara, Indonesia",
            "Tambang Sorin Pasadena, Kabupaten Bima, Pulau Sumbawa, Provinsi Nusa Tenggara Barat, Indonesia",
        ],
        "Malachite": [
            "Area Geunteut, Kabupaten Aceh Jaya, Provinsi Aceh, Indonesia",
            "Area Selogiri, Kabupaten Wonogiri, Provinsi Jawa Tengah, Indonesia",
            "Deposit Tuboh, Kabupaten Musi Rawas Utara, Provinsi Sumatra Selatan, Indonesia",
            "Deposit tembaga-molibdenum (Cu-Mo) Bulagidun, Talau, Provinsi Sulawesi Tengah, Indonesia",
            "Deposit Soripesa, Maria, Kabupaten Bima, Pulau Sumbawa, Provinsi Nusa Tenggara Barat, Indonesia",
        ],
        "Muscovite": [
            "Tambang emas Indo Muro, Kabupaten Barito Utara, Provinsi Kalimantan Tengah, Indonesia",
            "Pantai pesisir selatan, Kabupaten Waropen, Provinsi Papua, Indonesia",
            "Area Sangon, Kokap, Kabupaten Kulon Progo, Daerah Istimewa Yogyakarta, Indonesia",
            "Deposit porfiri tembaga-emas (Cu-Au) Elang, Kabupaten Sumbawa Barat, Pulau Sumbawa, Provinsi Nusa Tenggara Barat, Indonesia",
            "Batu Pancur, Pulau Belitung, Provinsi Bangka-Belitung, Indonesia",
        ],
        "Pyrite": [
            "Tambang Grasberg, Kompleks Ertsberg, Distrik Gunung Bijih (Distrik Grasberg), Kabupaten Mimika, Provinsi Papua, Indonesia",
            "Gunung Kuku, Batulicin, Kabupaten Tanah Bumbu, Provinsi Kalimantan Selatan, Indonesia",
            "Deposit Kelian, Provinsi Kalimantan Timur, Indonesia",
            "Gunung Papandayan, Kabupaten Garut, Provinsi Jawa Barat, Indonesia",
            "Tambang Gunung Pongkor, Kabupaten Bogor, Provinsi Jawa Barat, Indonesia",
        ],
        "Quartz": [
            "Dom skarn, Kompleks Ertsberg, Distrik Gunung Bijih (Distrik Grasberg), Kabupaten Mimika, Provinsi Papua, Indonesia",
            "anjung Balit, Kabupaten Lima Puluh Kota, Provinsi Sumatra Barat, Indonesia",
            "Ladang berlian Cempaka, Riam Kanan, Provinsi Kalimantan Selatan, Indonesia",
            "Kawah Ijen (Gunung Ijen), Kabupaten Banyuwangi, Provinsi Jawa Timur, Indonesia",
            "Deposit Bawone, Kabupaten Kepulauan Sangihe, Provinsi Sulawesi Utara, Indonesia",
        ]
    }

    # Buat tombol untuk setiap mineral
    for mineral, locations in mineral_locations.items():
        if st.button(f"Lokasi {mineral}"):
            st.subheader(f"Lokasi Persebaran {mineral}")
            for location in locations:
                st.write(f"- {location}")

    # Menambahkan legenda warna
    st.markdown("""
        <div class='section'>
            <h3>Keterangan Warna:</h3>
            <ul>
                <li style="color: blue;">Bornite - Biru</li>
                <li style="color: black;">Biotite - Hitam</li>
                <li style="color: red;">Chrysocolla - Merah</li>
                <li style="color: green;">Malachite - Hijau</li>
                <li style="color: purple;">Muscovite - Ungu</li>
                <li style="color: orange;">Pyrite - Orens</li>
                <li style="color: #cd4662;">Quartz - Merah Muda</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <div class='notes'>
            <i>Catatan:</i> Lokasi persebaran mineral yang dicantumkan hanya 5 lokasi untuk setiap mineral.
            Data ini merupakan sampel untuk tujuan informasi.
    """, unsafe_allow_html=True)