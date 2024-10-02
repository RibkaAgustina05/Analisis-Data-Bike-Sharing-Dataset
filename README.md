# Proyek Analisis Data: Tren Penyewaan Sepeda🚴‍♂️

Proyek bertujuan untuk mengeksplorasi kondisi cuaca (weathersit) memengaruhi jumlah penyewaan sepeda dan distribusi jumlah pengguna sepeda per jam (cnt) di berbagai jam dalam sehari?

## Fitur Utama 🚀

- **Pertanyaan Bisnis**: Proyek ini fokus pada dua pertanyaan utama:
- Apakah kondisi cuaca (weathersit) memengaruhi jumlah penyewaan sepeda?
- Bagaimana distribusi jumlah pengguna sepeda per jam (cnt) di berbagai jam dalam sehari?
- **Import Data & Wrangling**: Proses memuat, menilai, dan membersihkan data dilakukan secara bertahap, termasuk penghapusan kolom yang tidak diperlukan seperti `instant`.
- **Exploratory Data Analysis (EDA)**: Bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda, melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

- **Regresi Linear**: Proyek ini melakukan analisis regresi linear untuk memodelkan hubungan antara suhu dan jumlah penyewa sepeda harian.

- **Visualisasi Interaktif**: Menggunakan **Streamlit** untuk menghasilkan visualisasi dan analisis interaktif.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:

- `notebook.ipynb`: Jupyter Notebook yang berisi analisis mendalam terkait tren penyewaan sepeda.
- `data/`: Direktori yang berisi dataset penyewaan sepeda.
  - `day.csv`: Dataset penyewaan sepeda harian.
  - `hour.csv`: Dataset penyewaan sepeda per jam.
- `dashboard.py`: Script Python untuk menjalankan dashboard interaktif menggunakan **Streamlit**.
- `README.md`: Dokumentasi proyek ini.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek ini.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook

Untuk menjalankan analisis di **Jupyter Notebook**:

1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit

Proyek ini juga menyediakan dashboard interaktif menggunakan **Streamlit**. Ikuti langkah berikut untuk menjalankannya:

1. Instal semua dependensi menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi **Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

## Insight Utama 📊

1.  **Apakah kondisi cuaca (weathersit) memengaruhi jumlah penyewaan sepeda?**:

Ya berpengaruh,Cuaca cerah menghasilkan penyewaan sepeda tertinggi, Cuaca berkabut atau berawan menurunkan jumlah penyewaan sepeda.Cuaca buruk (seperti hujan) membuat orang lebih jarang menyewa sepeda.

2. **Bagaimana distribusi jumlah pengguna sepeda per jam (cnt) di berbagai jam dalam sehari?**:

   Penyewaan sepeda paling tinggi di pagi hari (jam 8) dan sore hari (jam 17), kemungkinan untuk perjalanan kerja atau sekolah. Penyewaan menurun di siang hari dan sangat rendah pada malam hari.

## Dataset

Dataset yang digunakan dalam proyek ini adalah:

- **day.csv**: Dataset harian yang mencatat data penyewaan sepeda termasuk informasi tentang suhu, kondisi cuaca, dan status hari libur.
- **hour.csv**: Dataset per jam yang mencatat data penyewaan sepeda per jam, memberikan detail yang lebih spesifik terkait waktu.

## Library yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk analisis dan visualisasi data.
- **Streamlit**: Library Python untuk membuat aplikasi web interaktif.
- **Matplotlib & Seaborn**: Digunakan untuk visualisasi data.
- **Pandas**: pustaka sumber terbuka yang digunakan untuk analisis dan manipulasi data.
- **Seaborn**: pustaka visualisasi data Python yang berbasis pada matplotlib
