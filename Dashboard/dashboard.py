import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Proyek Analisis Data: Bike Sharing Dataset")
st.text('Nama: Muhammad Dafa Rachman')
st.text('Email: daffarachman6654321@gmail.com')
st.text('ID Dicoding: MC314D5Y0997')

st.header("Pertanyaan Bisnis")
st.subheader("1. Bagaimana tren peminjaman sepeda berdasarkan setiap musim?")
st.subheader("2. Pada jam berapa peminjaman sepeda yang paling tinggi?")

day_df = pd.read_csv("Dashboard/day_cleared.csv")
hour_df = pd.read_csv("Dashboard/hour_cleared.csv")
tab1, tab2, tab3 = st.tabs(["Dataset", "Visualisasi", "Conclusion"]) 

with tab1:
    st.header("Dataset")

    st.subheader("Dataset day.csv")
    st.dataframe(day_df)

    st.subheader("Dataset hour.csv")
    st.dataframe(hour_df)

    with st.expander("Insight Dataset"):
        st.markdown(
                """
                **Deskripsi Atribut Dataset:**
                - **instant** = Nomor indeks
                - **dtday** = Tanggal dengan format YYY-MM-DD
                - **season** = Musim dengan kode angka (angka 1 untuk musim semi, angka 2 untuk musim panas, angka 3 untuk musim gugur, dan angka 4 untuk musim dingin)
                - **yr** = Tahun, dengan angka 0 untuk tahun 2011, dan angka 1 untuk tahun 20122
                - **mnth** = bulan
                - **holiday** = Apakah hari tersebut libur atau bukan
                - **weekday** = Hari dalam seminggu
                - **workingday** = Hari kerja 1, selainnya 0
                - **weatherlist** = kondisi cuaca:
                    - 1: Cerah, sedikit berawan, berawan sebagian
                    - 2: Berkabut + berawan, berkabut + awan terputus, berkabut + sedikit berawan
                    - 3: Salju ringan, hujan ringan + badai petir + awan tersebar, hujan ringan + awan tersebar
                    - 4: Hujan deras + butiran es + badai petir + kabut, salju + kabut
                - **temp** = Suhu yang diubah dalam Celsius, dihitung dengan rumus: (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
                - **atemp** = feeling temperature yang diubah menjadi Celsius, dihitung dengan (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
                - **hum** = kelembapan yang dinormalisasi, nilainya dibagi dengan 100 (max)
                - **windspeed** = kecepatan angin, nilainya dibagi dengan 67 (max)
                - **casual** = jumlah pengguna sepeda tidak terdaftar
                - **registered** = jumlah pengguna sepeda terdaftar
                - **cnt** = jumlah sepeda yang disewa, termasuk yang terdaftar dan tidak terdaftar
                """
            )


with tab2:
    st.header("Visualisasi")
    season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
    day_df["season_label"] = day_df["season"].map(season_labels)

    st.subheader("Tren peminjaman sepeda berdasarkan setiap musim")
    seasonal_trend = day_df.groupby("season_label")["cnt"].sum().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(x="season_label", y="cnt", data=seasonal_trend, palette="coolwarm", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Total Peminjaman")
    st.pyplot(fig)

    st.subheader("Jam peminjaman sepeda yang paling tinggi")
    hour_trend = hour_df.groupby("hr")["cnt"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="hr", y="cnt", data=hour_trend, marker="o", color="green", ax=ax)
    ax.set_title("Peminjaman Sepeda Berdasarkan Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Total Peminjaman")
    ax.set_xticks(range(0, 24))
    ax.grid(True)
    st.pyplot(fig)
    
with tab3:
    st.subheader("Kesimpulan")
    
    st.write("""
    - **Peminjaman sepeda tertinggi terjadi pada musim gugur.** Peminjaman lebih rendah pada musim lainnya, kemungkinan karena cuaca yang kurang mendukung. Penyedia layanan sepeda dapat meningkatkan jumlah unit sepeda yang tersedia pada musim gugur untuk memenuhi permintaan yang lebih tinggi.
    
    - **Peminjaman meningkat drastis pada jam 8 pagi dan 5 sore.** Pola ini menunjukkan bahwa sepeda banyak digunakan untuk perjalanan ke dan dari tempat kerja atau sekolah. Penyedia layanan dapat menawarkan promo atau diskon khusus pada jam sibuk tersebut untuk menarik lebih banyak pengguna.
    """)
