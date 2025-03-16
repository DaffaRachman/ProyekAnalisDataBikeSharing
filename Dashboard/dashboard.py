import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Proyek Analisis Data: Bike Sharing Dataset")
st.text('Nama: Muhammad Dafa Rachman')
st.text('Email: daffarachman6654321@gmail.com')
st.text('ID Dicoding: MC314D5Y0997')

day_df = pd.read_csv("../day_cleared.csv")
hour_df = pd.read_csv("../hour_cleared.csv")

season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
day_df["season_label"] = day_df["season"].map(season_labels)

st.subheader("Pertanyaan 1 : Bagaimana tren peminjaman sepeda berdasarkan setiap musim?")
seasonal_trend = day_df.groupby("season_label")["cnt"].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x="season_label", y="cnt", data=seasonal_trend, palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
st.pyplot(fig)

st.subheader("Pertanyaan 2 : Pada jam berapa peminjaman sepeda yang paling tinggi?")
hour_trend = hour_df.groupby("hr")["cnt"].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=hour_trend, marker="o", color="green", ax=ax)
ax.set_title("Peminjaman Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Total Peminjaman")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)
