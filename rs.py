import streamlit as st
import pandas as pd


col1, col2, col3 = st.columns(3)
with col1:
    header = st.image("foto_profil/logo.png", caption='', use_column_width=True,)
with col2:
    st.info(':phone: Call Center [WhatsApp](https://wa.me/6287872624702)')
with col3:
    st.info(':rocket: Social Media [Instagram](https://instagram.com/aryudistira_)')
header = st.image("foto_profil/hide.png", caption='', use_column_width=True,)
st.sidebar.header(':rocket: Menu')
menu = st.sidebar.radio('Navigasi', ['Profil', 'Pendaftaran', 'Ruang Perawatan', 'Layanan Cepat'])
if menu == 'Profil':
    st.title("Profil Rumah Sakit")
    col1, col2 = st.columns(2)
    with col1:
        namaa = ['Sejarah', 'Info Lebih Lengkap']
        pilihan_nama = st.selectbox('', namaa)
        if pilihan_nama == 'Info Lebih Lengkap':
            st.write('Rumah Sakit Pendidikan Univeritas Nasional Karangturi didirikan pada tahun 1965 oleh sekelompok dokter dan tenaga medis yang berdedikasi. Awalnya, rumah sakit ini dimulai sebagai fasilitas medis kecil dengan beberapa ruang perawatan, fasilitas darurat sederhana, dan staf yang terbatas. Tujuan utama pendirian rumah sakit ini adalah memberikan perawatan kesehatan berkualitas kepada masyarakat setempat. Selama tahun-tahun pertama operasinya, Rumah Sakit ini mengalami perkembangan yang signifikan. Dalam upaya untuk memenuhi kebutuhan kesehatan yang semakin meningkat, fasilitas rumah sakit diperluas, ruang perawatan ditambah, dan peralatan medis yang lebih canggih diperoleh. Selain itu, tim medis yang terampil dan berpengalaman direkrut untuk memberikan perawatan yang lebih baik kepada pasien. Seiring waktu, Rumah Sakit Pendidikan Univeritas Nasional Karangturi terus berkembang menjadi rumah sakit terkemuka dalam wilayah tersebut. Fasilitasnya diperluas menjadi bangunan yang lebih besar dan modern dengan berbagai departemen dan unit layanan. Rumah sakit ini juga memperoleh sertifikasi dan akreditasi yang diakui secara nasional, menunjukkan standar kualitas yang tinggi dalam pelayanan kesehatan yang mereka berikan. Sejarah Rumah Sakit Pendidikan Univeritas Nasional Karangturi juga ditandai dengan peningkatan dalam teknologi medis dan inovasi. Rumah sakit ini mengadopsi sistem rekam medis elektronik, peralatan diagnostik yang mutakhir, dan prosedur bedah minimal invasif. Mereka terus berinvestasi dalam pengembangan teknologi medis dan berkolaborasi dengan institusi penelitian untuk memajukan ilmu kedokteran dan pengobatan. Selain memberikan perawatan medis yang berkualitas, Rumah Sakit Pendidikan Univeritas Nasional Karangturi juga berperan sebagai pusat pendidikan dan pelatihan bagi para profesional kesehatan. Mereka menyelenggarakan program residensi, magang, dan pelatihan kontinu untuk membantu pengembangan karier dan peningkatan pengetahuan tenaga medis. Hingga hari ini, Rumah Sakit Pendidikan Univeritas Nasional Karangturi terus berkomitmen untuk menyediakan pelayanan kesehatan yang unggul, didukung oleh tim medis yang berkualitas dan teknologi medis yang mutakhir. Mereka memegang teguh misi untuk meningkatkan kualitas hidup pasien dan melayani masyarakat dengan penuh empati dan integritas.')
        else:
            st.write('')
        so = ['Struktur Organisasi', 'Info Lebih Lengkap']
        pilihan_so = st.selectbox('', so)
        if pilihan_so == 'Info Lebih Lengkap':
           st.image("foto_profil/so.png", caption='', use_column_width=True,)
        else:
            st.write('')
    with col2:
        visi = ['Visi Misi', 'Info Lebih Lengkap']
        visimisi = st.selectbox('', visi)
        if visimisi == 'Info Lebih Lengkap':
            st.write(' **Visi**   yaitu           Terwujudnya Rumah Sakit yang Prima, Presisi, Maju, Modern dan Menjadi Pilihan Masyarakat. **Misi**          Menyediakan pelayanan kesehatan berkualitas tinggi kepada pasien dan masyarakat dengan mengutamakan keamanan, kepercayaan, dan kepuasan pasien sebagai prioritas utama. Kami berkomitmen untuk mempromosikan kesehatan dan menyediakan perawatan medis terbaik, yang didukung oleh tenaga medis dan fasilitas terkini.')
        
        else:
            st.write('')
        program = ['Kegiatan PKRS', 'Info Lebih Lengkap']
        pks = st.selectbox('', program)
        if pks == 'Info Lebih Lengkap':
            st.write('Promosi Kesehatan Rumah Sakit (PKRS) adalah upaya Rumah Sakit untuk meningkatkan kemampuan pasien, klien dan kelompok masyarakat sehingga pasien dapat mandiri dalam mempercepat kesembuhan dan rehabilitasinya, mandiri dalam meningkatkan kesehatan, mencegah masalah kesehatan, dan mengembangkan upaya kesehatan melalui pembelajaran sesuai sosial budaya masing-masing. Tujuan dari PKRS adalah terciptanya masyarakat rumah sakit yang menerapkan Perilaku Hidup Bersih dan Sehat melalui perubahan pengetahuan, sikap, dan perilaku pasien RS serta pemeliharaan lingkungan RS dan termanfaatkannya dengan baik semua pelayanan yang disediakan RS.')
            st.write('Adapun kegiatan – kegiatan PKRS adalah sebagai berikut:')
            st.write('Pencegahan dan penanganan penyakit Hipertensi pada lansia, kader dan masyarakat umum di Kota Semarang')
        else:
            st.write('')

elif menu == 'Pendaftaran':
    st.write('')
    st.info('Klik link untuk melakukan [Pendaftaran](https://forms.gle/R4SAuMVLeHtx6QuAA) secara online')
    st.write('')
    st.write('')
    st.write('')
    st.subheader('Jurnal Penelitian')
    st.write('Jurnal penelitian kesehatan berperan penting dalam menyebarkan pengetahuan ilmiah terkini di bidang kesehatan. Mereka mempublikasikan temuan dan hasil penelitian terbaru, memberikan akses kepada para profesional kesehatan, peneliti, praktisi, dan masyarakat umum untuk memperoleh informasi terkini mengenai isu-isu kesehatan yang relevan.')
    st.info('[Gaya Kepemimpinan yang Efektif dalam Meningkatkan Kinerja Perawat untuk Keselamatan Pasien](https://unkartur.ac.id/journal/index.php/jurmik/article/view/132)')
    st.info('[Role of Nurses in Providing Quality Nursing Care to Increase Patient Satisfaction](https://unkartur.ac.id/journal/index.php/jurmik/article/view/137)')
    st.info('[Analisis Faktor Penyebab Keterlambatan Pengembalian Berkas Rekam Medis Rawat Inap RSUD Bangil](https://unkartur.ac.id/journal/index.php/jurmik/article/view/136)')


elif menu == 'Ruang Perawatan':
    col1, col2, = st.columns(2)
    with col1:
        st.image("ruang inap/president.png", caption='', use_column_width=True,)
        st.image("ruang inap/executive.png", caption='', use_column_width=True,)
        st.image("ruang inap/kelas1.png", caption='', use_column_width=True,)
        st.image("ruang inap/kelas3.png", caption='', use_column_width=True)
    with col2:
        st.image("ruang inap/suites.png", caption='', use_column_width=True,)
        st.image("ruang inap/vip.png", caption='', use_column_width=True,)
        st.image("ruang inap/kelas2.png", caption='', use_column_width=True,)

elif menu == 'Layanan Cepat':
    st.title('Layanan Cepat')
    col1, col2, = st.columns(2)
    with col1:
        st.title('**Ambulans**')
        st.write('RS Pendidikan Univeritas Nasional Karangturi didukung oleh Layanan Ambulans dalam penyediaan transportasi medis darurat dan non darurat. Dengan misi untuk menyediakan kualitas tertinggi bagi keselamatan dan perawatan pasien kami. Layanan Ambulans kami terdiri atas tim dokter, perawat, dan pengemudi ambulans yang sangat terlatih dalam penyelamatan jiwa dan pertolongan pertama.')
        st.subheader(':red[Kontak: +62 87872624702]')
    with col2:
        st.image("layanan cepat/ambulans.png", caption='', use_column_width=True)
    col1, col2, = st.columns(2)
    with col1:
        st.title('Family Care')
        st.write('Khusus pelanggan layanan Family Care RS Pendidikan Univeritas Nasional Karangturi, kami memberikan fasilitas pengantaran obat sesuai dengan resep dokter yang selanjutnya akan diantar langsung ke rumah Anda tanpa dipungut biaya tambahan. Pelayanan Kunjungan Rumah Family Care RS Pendidikan Univeritas Nasional Karangturi dan pengantaran obat memiliki batasan wilayah tertentu')
        st.subheader(':red[kontak: +62 87872624702]')
    with col2:
        st.image("layanan cepat/familycare.png", caption='', use_column_width=True)

st.title('Layanan Unggulan')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("foto_profil/bedah.png", caption='Bedah Minimal Invasif', use_column_width=True,)
with col2:
    st.image("foto_profil/jantung terpadu rsdk.png", caption='Jantung Terpadu', use_column_width=True,)
with col3:
    st.image("foto_profil/onkologi terpadu rsdk.png", caption='Onkologi Terpadu', use_column_width=True,)
with col4:
    st.image("foto_profil/cangkok sumsum tulang.png", caption='Transplantasi Organ', use_column_width=True,)
st.title('Rujukan Nasional')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("rujukan_nasional/anak.png", caption='Anak', use_column_width=True,)
with col2:
    st.image("rujukan_nasional/gigi mulut.png", caption='Gigi dan Mulut', use_column_width=True,)
with col3:
    st.image("rujukan_nasional/gizi.png", caption='Klinik Gizi', use_column_width=True,)
with col4:
    st.image("rujukan_nasional/saraf.png", caption='Bedah Saraf', use_column_width=True,)
st.title('Layanan Lainnya')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("layanan_lainnya/kv.png", caption='Klinik Virtual', use_column_width=True,)
with col2:
    st.image("layanan_lainnya/daftar vaksin.png", caption='Pendaftaran Vaksinasi Covid 19', use_column_width=True,)
with col3:
    st.image("layanan_lainnya/skm.png", caption='Survei Kepuasan Masyarakat', use_column_width=True,)
with col4:
    st.image("layanan_lainnya/deteksi covid.png", caption='Chat Deteksi Dini Covid 19', use_column_width=True,)

st.info('Informasi Lebih Lanjut:')
col1, col2, col3 = st.columns(3)
with col1:
    st.info('**Selamat datang di RS Pendidikan Univeritas Nasional Karangturi**')
    st.write('Jl. Raden Patah No.182-192 Rejomulyo, Semarang Timur, Kota Semarang - 50127 Jawa Tengah, Indonesia')
with col2:
    st.info('**Kontak Kami**')
    st.write(':phone: Hubungi kami di [WhatsApp](https://wa.me/6287872624702)')
    st.write(':envelope: Email : aldiyudistira00.com')
with col3:
    st.info('**Jam Operasional**')
    st.write('Senin-Jumat Pukul 08.00-17.00 WIB')
    st.write('UGD 24 Jam')
    st.write('Jam Besuk Pukul 17.00-20.00 WIB')
    st.write(':red[NOTE]')
    st.write('Anak usia dibawah 14 tahun tidak diperkenankan masuk kedalam ruang perawatan, Terima kasih.')


st.header(":mailbox: Masukan saran!")

contact_form = """
<form action="https://formsubmit.co/aldiyudistira00@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Nama Lengkap" required>
     <input type="email" name="email" placeholder="Email Valid" required>
     <textarea name="message" placeholder="Tambahkan Saran"></textarea>
     <button type="submit">Kirim</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style/style.css")
