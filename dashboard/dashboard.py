import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setel gaya visualisasi untuk seaborn
sns.set_style('whitegrid')

# Memuat dataset
day_data = pd.read_csv('Bike-sharing-dataset/day.csv')
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Judul Dashboard
st.title('Dashboard Analisis Penggunaan Sepeda')

# Menampilkan dataset
st.write("## Gambaran Umum Dataset")
st.dataframe(day_data.head())

# Tren Penggunaan Sepeda
st.write("## Tren Penggunaan Sepeda Sepanjang Tahun")
fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(data=day_data, x='dteday', y='cnt', ax=ax)
ax.set(title='Tren Penggunaan Sepeda Sepanjang Tahun', xlabel='Tanggal', ylabel='Jumlah Pengguna')
st.pyplot(fig)

# Distribusi Pengguna Sepeda
st.write("## Distribusi Pengguna Sepeda")
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

sns.histplot(day_data['casual'], kde=True, ax=axs[0])
axs[0].set(title='Distribusi Pengguna Kasual', xlabel='Jumlah Pengguna Kasual', ylabel='Frekuensi')

sns.histplot(day_data['registered'], kde=True, ax=axs[1])
axs[1].set(title='Distribusi Pengguna Terdaftar', xlabel='Jumlah Pengguna Terdaftar', ylabel='Frekuensi')

sns.histplot(day_data['cnt'], kde=True, ax=axs[2])
axs[2].set(title='Distribusi Pengguna Total', xlabel='Jumlah Pengguna Total', ylabel='Frekuensi')

st.pyplot(fig)

# Penggunaan Sepeda Berdasarkan Musim
st.write("## Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_data, x='season', y='cnt', ax=ax)
ax.set(title='Penggunaan Sepeda Berdasarkan Musim', xlabel='Musim', ylabel='Jumlah Pengguna')
st.pyplot(fig)

# Penggunaan Sepeda pada Hari Kerja vs Hari Libur
st.write("## Penggunaan Sepeda pada Hari Kerja vs Hari Libur")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_data, x='workingday', y='cnt', ax=ax)
ax.set(title='Penggunaan Sepeda pada Hari Kerja vs Hari Libur', xlabel='Hari Kerja (0: Tidak, 1: Ya)', ylabel='Jumlah Pengguna')
st.pyplot(fig)

# Penggunaan Sepeda Berdasarkan Kondisi Cuaca
st.write("## Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=day_data, x='weathersit', y='cnt', ax=ax)
ax.set(title='Penggunaan Sepeda Berdasarkan Kondisi Cuaca', xlabel='Kondisi Cuaca', ylabel='Jumlah Pengguna')
st.pyplot(fig)

# Korelasi Antar Variabel
st.write("## Matriks Korelasi Antar Variabel")
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(day_data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
ax.set(title='Matriks Korelasi')
st.pyplot(fig)

# Footer
st.write("Dashboard ini dibuat untuk menganalisis penggunaan sepeda berdasarkan berbagai faktor seperti musim, hari kerja, dan kondisi cuaca.")
