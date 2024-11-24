import streamlit as st
import os
import numpy as np
from PIL import Image
import io
import tensorflow as tf

def load_model_and_classes(model_path= './data/model.h5'):
    """Memuat model dan daftar kelas"""
    model = tf.keras.models.load_model(model_path)
    class_names = ['biotite', 'bornite', 'chrysocolla', 'malachite', 'muscovite', 'pyrite', 'quartz']
    return model, class_names

def analyze_image(image, model, class_names, threshold=0.6):
    """Menganalisis gambar dan mengembalikan prediksi beserta kepercayaan."""
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    prediction = model.predict(np.expand_dims(image, axis=0))

    index = np.argmax(prediction)
    confidence = prediction[0][index]

    if confidence >= threshold:
        return class_names[index], confidence
    return None, None

def show_solution(predicted_class, class_names, confidence):
    """Menampilkan informasi tentang mineral berdasarkan prediksi."""
    mineral_info = {
        "biotite": """<div class='section', 'font'>
                        <div class='font'>
                        <h2>Informasi tentang Biotite</h2>
                        <p> Pernah dianggap sebagai mineral tersendiri, <strong>Biotite</strong> kini diakui sebagai seri larutan padat dengan mineral annite sebagai anggotaanggota akhir besi dan phlogopite sebagai anggota akhir magnesium.
                        Namanya diberikan pada tahun 1847 untuk menghormati fisikawan Prancis Jean-Baptiste Biot. Mika dari seri Biotite biasanya membentuk kristal besar berbentuk pipih hingga pendek dengan prisma, sering kali memiliki penampang pseudoheksagonal.
                        Mineral ini juga ditemukan dalam bentuk lapisan tipis, agregat bersisik, atau butiran yang tersebar. 
                        \nJenis biotite berwarna hitam jika kaya akan besi, selanjutnya berwarna cokelat, lalu kuning pucat hingga cokelat muda, atau perunggu dengan kandungan magnesium yang lebih tinggi.
                        Biotite mudah membelah menjadi lembaran tipis yang fleksibel.
                        Mika dari seri Biotite tersebar luas. Mereka merupakan komponen utama banyak batuan beku dan metamorf, termasuk granit,nepheline syenites, gneisses, dan schists. Mineral ini juga ditemukan dalam deposit hidrotermal yang kaya kalium dan beberapa batuan sedimen klastik.
                        <strong>Biotite banyak digunakan untuk menentukan usia batuan.</strong>
                        \n<strong>Rumus Kimia: <em>K(Fe2+/Mg)2(Al/Fe3+/Mg/Ti)([Si/Al/Fe]2Si2O10)(OH/F)2</em></strong></p>
                      </div></div>""",
        "bornite": """<div class='section'>
                        <div class='font'>
                        <h2>Informasi tentang Bornite</h2>
                        <p><strong>Bornite</strong> adalah sulfida besi tembaga yang dinamai sesuai dengan nama ahli mineralogi Austria, Ignaz von Born (1742-91). Bornite salah satu mineral yang paling berwarna di alam.
                        Sebuah bijih utama tembaga, yang warna alami bisa berwarna merah tembaga, coklat tembaga, atau perunggu. Bijih ini juga dapat menunjukkan percikan warna ungu, biru, dan merah yang berwarna-warni pada permukaan yang rusak dan ternoda, yang menjelaskan nama umumnya, 'bijih merak'.
                        Bornite juga dikenal sebagai “bijih tembaga ungu” dan “bijih tembaga beraneka ragam.” Kristal bornite jarang ditemukan. Meskipun mereka menunjukkan simetri ortorombik, kristal, ketika ditemukan, berbentuk kubik, oktahedral, atau dodecahedral, sering kali dengan permukaan yang melengkung atau kasar.
                        \nBornite sering kali berbentuk padat, granular, atau masif dan mudah berubah menjadi chalcocite dan mineral tembaga lainnya pada saat pelapukan. Bornit terbentuk terutama pada endapan bijih tembaga hidrotermal dengan mineral seperti chalcopyrite, pyrite, marcasite, dan quartz.
                        Hal ini juga terbentuk pada beberapa batuan beku intrusif yang miskin silika dan pada urat pegmatit dan zona metamorf kontak.
                        \n<strong>Rumus Kimia: <em>Cu5FeS4</em></strong>
                        </p>
                      </div></div>""",
        "chrysocolla": """<div class='section'>
                        <div class='font'>
                        <h2>Informasi tentang Chrysocolla</h2>
                        <p>Istilah <strong>Chrysocolla</strong> pertama kali digunakan oleh filsuf Yunani Theophrastus pada tahun 315 SM untuk merujuk pada berbagai bahan yang digunakan dalam penyolderan emas. 
                        Nama ini berasal dari dua kata Yunani: chrysos, yang berarti "emas," dan kolla, yang berarti "lem." Chrysocolla adalah silikat aluminium tembaga, yang umumnya berwarna hijau-biru.
                        Spesimen biasanya berbutir halus dan bersifat massal. Kristal ini sangat jarang ditemukan, tetapi jika ada, mereka muncul dalam bentuk agregat botrioidal yang memancar.
                        Chrysocolla, yang kadang-kadang menjadi bijih tembaga, merupakan produk dekomposisi mineral tembaga, terutama di daerah kering.
                        Chrysocolla sering menyatu dengan mineral lain, seperti quartz , chalcedony , dan opal, untuk menghasilkan jenis batu permata. Batu permata ini dapat memiliki berat lebih dari 5 lb (2,3 kg).
                        \n<strong>Rumus Kimia: <em>Cu2-xAlx(H2-xSi2O5)(OH)4 · nH2O, x < 1</em></strong>
                        </p>
                        </div></div>""",
        "malachite": """<div class='section'>
                        <div class='font'>
                        <h2>Informasi tentang Malachite</h2>
                        <p><strong>Malachite</strong> -- 'Kemungkinan bijih tembaga yang paling awal'. Malachite diyakini telah ditambang di Sinai dan gurun timur Mesir kuno sejak tahun 3000 SM.
                        Kristal tunggal jarang ditemukan; ketika ditemukan, kristal tersebut berbentuk prisma pendek hingga panjang.
                        Malachite biasanya ditemukan sebagai massa botryoidal atau bertatahkan, sering kali dengan struktur berserat yang memancar dan berpita dalam berbagai warna hijau.
                        Malachite juga muncul sebagai agregat berserat halus dan sebagai stalaktit yang berpita secara konsentris. Malachite muncul di zona-zona yang berubah dari endapan tembaga, di mana biasanya disertai dengan jumlah azurit yang lebih sedikit.
                        Malachite dihargai sebagai bahan ornamen dan batu permata. Massa tunggal dengan berat hingga 51 ton ditemukan di Pegunungan Ural, Rusia, pada abad ke-19.
                        \n<strong>Rumus Kimia: <em>Cu2(CO3)(OH)2</em></strong>
                        </p>
                      </div></div>""",
        "muscovite": """<div class='section'>
                        <div class='font'>
                        <h2>Informasi tentang Muscovite</h2>
                        <p><strong>Muscovite</strong> juga dikenal sebagai mica umum, mika potas, atau isinglass. Muscovite adalah anggota paling umum dari kelompok mika.
                        Spesimennya biasanya tidak berwarna atau putih keperakan, tetapi juga dapat berwarna cokelat, abu-abu muda, hijau pucat, atau merah mawar.
                        Muskovit biasanya ditemukan dalam bentuk kristal pipih dengan bentuk heksagonal atau pseudoheksagonal. Kristalnya bisa mencapai diameter hingga 3 meter.
                        Muskovit juga dapat terbentuk sebagai lembaran tipis dan agregat berbutir halus. 
                        \nMuskovit berbutir halus disebut serisit atau mika putih, sedangkan spesimen berwarna hijau cerah yang kaya kromium disebut fuchsite.
                        Sebagai mineral pembentuk batuan yang umum, muskovit ditemukan pada batuan metamorf seperti gneisses dan schists, serta pada granit, veins, dan pegmatites.
                        Mineral ini juga ditemukan dalam beberapa sedimen berbutir halus. Muskovit memiliki nilai komersial yang cukup besar. Kandungan besi yang rendah membuatnya menjadi isolator listrik dan termal yang baik. Di Rusia, lembaran muskovit tipis dan transparan, yang disebut kaca muscovy, pernah digunakan sebagai kaca jendela.
                        \n<strong>Rumus Kimia: <em>KAl2(AlSi3O10)(OH)2</em></strong>
                        </p>
                      </div></div>""",
        "pyrite": """<div class='section'>
                      <div class='font'>
                      <h2>Informasi tentang Pyrite</h2>
                      <p>Dikenal sejak zaman kuno, <strong>Pyrite</strong> biasanya disebut sebagai “emas bodoh”. Meskipun jauh lebih ringan daripada emas, warnanya yang seperti kuningan dan kepadatannya yang relatif tinggi telah menyesatkan banyak penambang pemula.
                        Namanya berasal dari kata Yunani pyr, yang berarti “api”, karena mengeluarkan percikan api saat dipukul dengan besi. Warnanya buram dan kuning keperakan pucat saat masih segar, berubah menjadi lebih gelap dan menodai jika terpapar oksigen. 
                        Kristal Pyrite dapat berbentuk kubik, oktahedral, atau “pyritohedra” bersisi dua belas, dan sering kali berbentuk lurik. Pyrite juga dapat berbentuk masif atau granular, atau membentuk cakram pipih atau bintil-bintil kristal memanjang yang memancar.
                        Pyrite terjadi dalam urat hidrotermal, melalui pemisahan dari magma, dalam batuan metamorf kontak, dan dalam batuan sedimen, seperti serpih, dan batu bara, di mana ia dapat mengisi atau menggantikan fosil.
                        \n<strong>Rumus Kimia: <em>FeS2</em></strong>
                        </p>
                     </div></div>""",
        "quartz": """<div class='section'>
                      <div class='font'>
                      <h2>Informasi tentang Quartz</h2>
                      <p><strong>Quartz</strong> adalah salah satu mineral paling umum di kerak Bumi, Quartz memiliki dua bentuk: Makrokristalin (dengan kristal yang dapat dilihat oleh mata) dan
                        Kriptokristalin(terbentuk dari kristal mikroskopis). Quartz Makrokristalin biasanya tidak berwarna dan transparan, seperti pada kristal batu, atau putih dan tembus cahaya, seperti pada Quartz susu.
                        \nQuartz jenis berwarna meliputi: 
                        \n- Quartz mawar yang berwarna merah muda dan tembus cahaya,
                        \n- Quartz Ametis berwarna ungu atau lavender yang transparan hingga tembus cahaya,
                        \n- Quartz berasap berwarna hitam atau coklat yang transparan hingga tembus cahaya,
                        \n- Sitrin berwarna kuning atau kuning-coklat yang transparan hingga tembus cahaya.
                        \n Semua jenis kristalin membentuk prisma dan piramida heksagonal. Jenis quartz kriptokristalin meliputi  chalcedony, agate, dan jasper. Quartz terdapat di hampir semua batuan sedimen, beku, dan metamorf yang kaya akan silika.
                        \n<strong>Rumus Kimia: <em>SiO2</em></strong>
                        </p>
                     </div></div>"""
    }

    # Mendapatkan informasi mineral yang sesuai
    info = mineral_info.get(predicted_class, "<div class='section'><h2>Informasi Tidak Tersedia</h2></div>")
    # Menampilkan informasi menggunakan HTML
    st.markdown(info, unsafe_allow_html=True)

def load_css(file_path):
    """Memuat file CSS untuk styling halaman."""
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def show_analyze():
    """Halaman utama untuk deteksi mineral."""
    # Menentukan path file
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    css_path = os.path.join(parent_dir, "../resources/style/style.css")
    load_css(css_path)

    st.title("🔍 Mulai Deteksi Mineral Anda")
    st.markdown("Unggah gambar mineral untuk mencoba fitur deteksi dan klasifikasi mineral kami secara langsung.")

    st.markdown("""
            <div class='subheader'><h3>Disclaimer</h3></div>""", unsafe_allow_html=True)
    st.markdown("""        
            <div class='font'><p>Pada aplikasi ini, model AI hanya dapat mendeteksi 7 kelas mineral, yaitu sebagai berikut:
            \n- Biotite
            \n- Bornite
            \n- Chrysocolla
            \n- Malachite
            \n- Muscovite
            \n- Pyrite
            \n- Quartz 
            \nSetiap gambar mineral yang diunggah akan dianalisis untuk menentukan jenis mineral yang sesuai dari tujuh kelas di atas.</p></div>""", unsafe_allow_html=True)

    # Memuat model dan daftar kelas
    model, class_names = load_model_and_classes()

    threshold = 0.6
    option = st.selectbox("Pilih pengambilan gambar", ["Upload foto", "Ambil foto"], help="Pilih metode untuk memasukkan gambar.")

    if option == "Upload foto":
        with st.container():
            st.markdown('<div class="short-upload">', unsafe_allow_html=True)
            uploaded_file = st.file_uploader("Upload gambar mineral", type=['jpg', 'jpeg', 'png'], label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

            if uploaded_file:
                pil_image = Image.open(io.BytesIO(uploaded_file.read())).convert('RGB')
                st.image(pil_image, caption="Gambar yang diunggah", use_column_width="auto")

                # Tombol Analisis Gambar
                if st.button("Analisis Gambar"):
                    predicted_class, confidence = analyze_image(pil_image, model, class_names, threshold)
                    if predicted_class:
                        st.success(f"Prediksi: {predicted_class} ({confidence * 100:.2f}%)")
                        show_solution(predicted_class, class_names, confidence)
                    else:
                        st.warning("Mineral tidak terdeteksi.")

    elif option == "Ambil foto":
        image_captured = st.camera_input("Capture a photo", label_visibility="collapsed")
        if image_captured:
            pil_image = Image.open(io.BytesIO(image_captured.getvalue())).convert('RGB')
            st.image(pil_image, caption="Foto yang diambil", use_column_width="auto")

            if st.button("Analisis Gambar"):
                predicted_class, confidence = analyze_image(pil_image, model, class_names, threshold)
                if predicted_class:
                    st.success(f"Prediksi: {predicted_class} ({confidence * 100:.2f}%)")
                    show_solution(predicted_class, class_names, confidence)
                else:
                    st.warning("Mineral tidak terdeteksi.")

    st.markdown("""
        <div class='notes'>
            <i>Catatan:</i> Informasi Mineral didapatkan dari buku <strong>NATUREGUIDE ROCKS AND MINERALS-Ronald Louis Bonewitz</strong> dan 
                Website: <strong>https://www.mindat.org</strong>
    """, unsafe_allow_html=True)