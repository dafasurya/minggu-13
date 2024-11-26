import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Menyiapkan dataset dan gambar
dataset_path = "CarPrice.csv"
image_path = "hamster.jpg"

# Membaca dataset
df = pd.read_csv(dataset_path)

# Sidebar menu
st.sidebar.title("Select Page")
page = st.sidebar.selectbox("Menu", ["Home", "Dataset", "Graph"])

# Halaman Home
if page == "Home":
    st.title("Welcome to Car Price Analysis")
    st.image(image_path, caption="Car Price Analysis", use_container_width=True)

# Halaman Dataset
elif page == "Dataset":
    st.title("Dataset: Car Prices")
    st.dataframe(df)  # Menampilkan dataset

# Halaman Graph
elif page == "Graph":
    st.title("Car Prices Analysis")

    # Contoh visualisasi: Average price by brand
    st.subheader("Average Price by Brand")
    avg_price = df.groupby("CarName")["price"].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    avg_price.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Average Price by Car Brand")
    ax.set_xlabel("Car Brand")
    ax.set_ylabel("Average Price")
    st.pyplot(fig)
