import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style visualisasi
sns.set(style='whitegrid')

# Judul untuk Aplikasi Streamlit
st.title('Proyek Analisis Data Penyewaan Sepeda')

# Load datasets
st.header('1. Mengimpor Data')
day_df = pd.read_csv('Data/day.csv')
hour_df = pd.read_csv('Data/hour.csv')

st.write("Dataset 'day.csv':")
st.dataframe(day_df.head())

st.write("Dataset 'hour.csv':")
st.dataframe(hour_df.head())

# Assessing the basic statistics of both datasets
st.header('2. Statistik Dasar')
st.subheader("Statistik Dasar - day.csv")
st.write(day_df.describe())

st.subheader("Statistik Dasar - hour.csv")
st.write(hour_df.describe())

# Data Wrangling: Cleaning Data
st.header('3. Data Cleaning')
st.write("Missing values in day.csv:")
st.write(day_df.isnull().sum())

st.write("\nMissing values in hour.csv:")
st.write(hour_df.isnull().sum())

# Dropping missing values
day_df_clean = day_df.dropna()
hour_df_clean = hour_df.dropna()

# Check for duplicates
st.write("\nChecking for duplicates in day.csv:")
st.write(day_df_clean.duplicated().sum())

st.write("\nChecking for duplicates in hour.csv:")
st.write(hour_df_clean.duplicated().sum())

# Drop duplicates
day_df_clean = day_df_clean.drop_duplicates()
hour_df_clean = hour_df_clean.drop_duplicates()

# Correlation and Heatmap
st.header('4. Analisis Korelasi')
st.subheader('Correlation Matrix - day.csv')
numerical_cols_day = day_df_clean.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_cols_day.corr(), annot=True, cmap='coolwarm', fmt='.2f', 
            annot_kws={"size": 10}, linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.title('Correlation Matrix - day.csv', fontsize=12)
plt.tight_layout()
st.pyplot(plt)

st.subheader('Correlation Matrix - hour.csv')
numerical_cols_hour = hour_df_clean.select_dtypes(include=['float64', 'int64'])
plt.figure(figsize=(10, 6))
sns.heatmap(numerical_cols_hour.corr(), annot=True, cmap='coolwarm', fmt='.2f', 
            annot_kws={"size": 10}, linewidths=0.5, cbar_kws={'shrink': 0.8})
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(rotation=0, fontsize=10)
plt.title('Correlation Matrix - hour.csv', fontsize=12)
plt.tight_layout()
st.pyplot(plt)

# Menghitung rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca (weathersit)
st.header('5. Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda')
weather_group = day_df_clean.groupby('weathersit')['cnt'].mean().reset_index()
colors = ['lightgreen' if cnt != weather_group['cnt'].max() else 'darkgreen' for cnt in weather_group['cnt']]

# Membuat plot untuk melihat hubungan antara kondisi cuaca dan jumlah penyewaan sepeda
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=weather_group, palette=colors)  
plt.title('Pengaruh Kondisi Cuaca (weathersit) terhadap Jumlah Penyewaan Sepeda (cnt)')
plt.xlabel('Kondisi Cuaca (weathersit)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda (cnt)')
plt.xticks(ticks=[0, 1, 2], labels=['Clear/Good', 'Mist/Cloudy', 'Bad Weather'])  
st.pyplot(plt)

# Visualisasi Data - Distribusi Jumlah Pengguna Sepeda per Jam dalam Sehari
st.header('6. Distribusi Jumlah Pengguna Sepeda per Jam dalam Sehari')

# Menghitung rata-rata jumlah penyewaan sepeda per jam
hour_group = hour_df_clean.groupby('hr')['cnt'].mean().reset_index()

# Membuat plot untuk melihat distribusi jumlah pengguna sepeda per jam dalam sehari
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hour_group, marker='o', color='b')
plt.title('Distribusi Rata-rata Jumlah Pengguna Sepeda per Jam dalam Sehari')
plt.xlabel('Jam dalam Sehari (hr)')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda (cnt)')
plt.xticks(range(0, 24))  
plt.grid(True)
st.pyplot(plt)
