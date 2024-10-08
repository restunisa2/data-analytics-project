#Membuat Dashboard pada Streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
day_df = pd.read_csv("https://drive.usercontent.google.com/download?id=1qDM1Vn6406Nr55dxq0WMmOufbXUScQDm&export=download&authuser=0&confirm=t&uuid=d42dd168-0e26-4589-8eb8-09afca15eacd&at=AN_67v0YTtQpVQn5En07gbUVipYG:1728288790069")
hour_df = pd.read_csv("https://drive.usercontent.google.com/download?id=1CFCpCsUS78O1DctQGFOH3cQ1t0pY13O-&export=download&authuser=0&confirm=t&uuid=d3b087fe-664e-43fb-b87f-4d93667719e7&at=AN_67v0_hSiXKvqwdg0jLcT3zunZ:1728288863401")

# Membuat judul aplikasi
st.title("Bike Sharing Analysis Dashboard")

# Sidebar dengan filter (opsional)
st.sidebar.header("Filter")
selected_year = st.sidebar.selectbox("Pilih Tahun", [2011, 2012])

# Bagian 1: Analisis Musim
st.header("Analisis Musim")

# Boxplot untuk musim dan jumlah penyewaan
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season', y='cnt', data=day_df, ax=ax)
plt.title('Jumlah Penyewaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.grid(True)
st.pyplot(fig)

# Bar plot untuk rata-rata penyewaan berdasarkan musim
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
season_day = day_df.groupby(by='season').agg({"cnt": "mean"}).reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=season_day, ax=ax)
plt.title('Rata-rata Jumlah Penyewaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.xticks([0, 1, 2, 3], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.show()
st.pyplot(fig)

# Bagian 2: Analisis Tren Harian
st.header("Analisis Tren Harian")

# Line plot untuk tren harian
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
tren_jam = hour_df.groupby(by='hr').agg({"cnt": "mean"})
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=tren_jam, marker='o', ax=ax)
plt.title('Tren Rata-rata Penyewaan Sepeda Berdasarkan Waktu dalam Sehari')
plt.xlabel('Jam (hr)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.xticks(range(0, 24))
plt.grid(True)
st.pyplot(fig)

# Line plot untuk tren harian dengan perbandingan tahun
st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Jam (2011 vs 2012)")
tren_jam_pertahun = hour_df.groupby(['yr', 'hr']).agg({"cnt": "mean"}).reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', hue='yr', data=tren_jam_pertahun, marker='o', ax=ax)
plt.title('Tren Rata-rata Penyewaan Sepeda Berdasarkan Waktu dalam Sehari (2011 vs 2012)')
plt.xlabel('Jam (hr)')
plt.ylabel('Rata-rata Jumlah Penyewaan Sepeda')
plt.xticks(range(0, 24))
plt.legend(labels=['2011', '2012'], title='Tahun')
plt.grid(True)
st.pyplot(fig)
