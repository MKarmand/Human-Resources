
# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

🔗 [Klik di sini untuk melihat dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)
🔗 [Klik di sini untuk melihat dashboard Tableau](https://public.tableau.com/app/profile/muhammad.armand7202/viz/MKAHR/HRAnalyticsDashboard)
🔗 [Klik di sini untuk melihat web streamlit](https://human-resources-mka.streamlit.app/)

## Business Understanding

Perusahaan Edutech mengalami tingkat pergantian karyawan (employee attrition) yang cukup tinggi. Hal ini menyebabkan terganggunya stabilitas tim dan meningkatnya biaya rekrutmen. Untuk mengatasi masalah tersebut, dilakukan analisis data SDM dan pembangunan model prediksi untuk mengidentifikasi karyawan yang berpotensi keluar.

### Permasalahan Bisnis

- Tingginya tingkat attrition karyawan di perusahaan.
- Kurangnya pemahaman mengenai faktor-faktor yang memengaruhi keputusan karyawan untuk keluar.
- Belum adanya sistem prediksi untuk mengidentifikasi karyawan berisiko tinggi keluar.

### Cakupan Proyek

- Membersihkan dan menyiapkan dataset karyawan.
- Membangun model prediksi attrition menggunakan Random Forest Classifier.
- Memprediksi data karyawan yang belum berlabel.
- Visualisasi data melalui business dashboard menggunakan Tableau Public.

### Persiapan


**Sumber Data:**

Dataset yang digunakan dalam proyek ini adalah dataset Human Resources Employee Attrition. Dataset ini berisi informasi mengenai karyawan, termasuk data demografis, riwayat pekerjaan, dan faktor-faktor lain yang relevan dengan attrition.



**Setup Environment:**

Untuk menjalankan proyek ini perlu menyiapkan environment pengembangan dengan langkah-langkah berikut:

python3 -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate   # Untuk Windows

**Install library yang dibutuhkan dari requirements.txt**

pip install -r requirements.txt

**Jalankan file menggunakan python**

python humanrecourcesdatascience.py

## Business Dashboard

Business dashboard dibuat menggunakan **Tableau Public** untuk memvisualisasikan hasil prediksi dan statistik karyawan. Dashboard mencakup:

- Tingkat attrition secara keseluruhan.
- Distribusi karyawan berdasarkan departemen, usia, dan jabatan.
- Perbandingan karakteristik antara karyawan yang keluar dan yang bertahan.


## Conclusion

Model klasifikasi yang dibangun dengan algoritma Random Forest berhasil memprediksi attrition karyawan berdasarkan data historis. Model ini mampu membantu manajemen dalam mengidentifikasi karyawan yang berisiko tinggi untuk keluar. Dengan demikian, intervensi preventif dapat dilakukan lebih awal.

### Rekomendasi Action Items (Optional)

- Melakukan analisis mendalam terhadap fitur-fitur penting seperti WorkLifeBalance dan JobSatisfaction.
- Menyusun strategi retensi karyawan berdasarkan hasil prediksi.
- Mengembangkan sistem peringatan dini berbasis model prediksi untuk HRD.
- Melanjutkan pengumpulan dan pembaruan data untuk meningkatkan akurasi model.
