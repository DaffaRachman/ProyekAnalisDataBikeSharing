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
tab1, tab2 = st.tabs(["Visualisasi", "Conclusion"]) 

with st.sidebar :
    st.header("Filter Data")
    selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua Musim", "Semi", "Panas", "Gugur", "Dingin"])
    selected_hour = st.sidebar.multiselect("Pilih Jam:", sorted(hour_df["hr"].unique()))
    
    label = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
    day_df["season_label"] = day_df["season"].map(label)
    hour_df["season_label"] = hour_df["season"].map(label)

    if selected_season != "Semua Musim":
        day_df = day_df[day_df["season_label"] == selected_season]
        hour_df = hour_df[hour_df["season_label"] == selected_season]
    
    if selected_hour:
        hour_df = hour_df[hour_df["hr"].isin(selected_hour)]

    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

    start_date = day_df["dteday"].min().date()
    end_date = day_df["dteday"].max().date()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=start_date,
        max_value=end_date,
        value=[start_date, end_date]
    )

    day_filtered = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                        (day_df["dteday"] <= pd.to_datetime(end_date))]
    hour_filtered = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                         (hour_df["dteday"] <= pd.to_datetime(end_date))]
    
with tab1:
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

    st.subheader("Tren peminjaman sepeda berdasarkan setiap musim")
    season_trend = day_df.groupby("season_label")["cnt"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x="season_label", y="cnt", data=season_trend, marker="o", color="green", ax=ax)
    ax.set_title("Peminjaman Sepeda Berdasarkan Jam")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Total Peminjaman")
    # ax.set_xticks(range(0, 24))
    ax.grid(True)
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

with tab2:
    st.subheader("Kesimpulan")
    
    st.write("""
    - **Peminjaman sepeda tertinggi terjadi pada musim gugur.** Peminjaman lebih rendah pada musim lainnya, kemungkinan karena cuaca yang kurang mendukung. Penyedia layanan sepeda dapat meningkatkan jumlah unit sepeda yang tersedia pada musim gugur untuk memenuhi permintaan yang lebih tinggi.
    
    - **Peminjaman meningkat drastis pada jam 8 pagi dan 5 sore.** Pola ini menunjukkan bahwa sepeda banyak digunakan untuk perjalanan ke dan dari tempat kerja atau sekolah. Penyedia layanan dapat menawarkan promo atau diskon khusus pada jam sibuk tersebut untuk menarik lebih banyak pengguna.
    """)
