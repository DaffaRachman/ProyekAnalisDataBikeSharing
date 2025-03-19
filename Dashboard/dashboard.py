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

    # Menampilkan insight dengan expander
    with st.expander("Insight Dataset"):
        st.markdown(
            """
            **Deskripsi Atribut Dataset:**
            - **instant** = Nomor indeks
            - **dteday** = Tanggal dengan format YYYY-MM-DD
            - **season** = Musim (1: Semi, 2: Panas, 3: Gugur, 4: Dingin)
            - **yr** = Tahun (0: 2011, 1: 2012)
            - **mnth** = Bulan (1-12)
            - **holiday** = Hari libur (0: Tidak, 1: Ya)
            - **weekday** = Hari dalam seminggu (0-6, Minggu-Sabtu)
            - **workingday** = Hari kerja (1: Ya, 0: Tidak)
            - **weatherlist** = Kondisi cuaca:
                - 1: Cerah, sedikit berawan, berawan sebagian
                - 2: Berkabut + berawan / sedikit berawan
                - 3: Hujan ringan, salju ringan, badai petir
                - 4: Hujan deras, badai petir, kabut, salju
            - **temp** = Suhu dalam Celsius, dinormalisasi dengan (t-t_min)/(t_max-t_min)
            - **atemp** = Feeling temperature dalam Celsius, dinormalisasi
            - **hum** = Kelembapan (dinormalisasi)
            - **windspeed** = Kecepatan angin (dinormalisasi)
            - **casual** = Jumlah pengguna sepeda tidak terdaftar
            - **registered** = Jumlah pengguna sepeda terdaftar
            - **cnt** = Total jumlah peminjaman sepeda (casual + registered)
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
