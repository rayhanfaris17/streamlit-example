pip install google-generativeai streamlit

import google.generativeai as palm

palm.configure(api_key="AIzaSyDCU-MMzjRH-glaOpWI4FlEm76eNcUJlMI")

import streamlit as st
import requests

# Fungsi untuk memanggil model AI (Palm 2)
def generate_resep(ingredients):
    # Ganti URL_API dengan URL yang sesuai untuk model AI Palm 2 Anda
    url_api = "api_key"
    payload = {"ingredients": ingredients}
    response = requests.post(url_api, json=payload)

    if response.status_code == 200:
        return response.json()["resep"]
    else:
        return "Gagal menghasilkan resep. Silakan coba lagi."

# Tampilan UI menggunakan Streamlit
def main():
    st.title("Chef AI - Generate Resep")

    # Input dari pengguna
    ingredients = st.text_area("Masukkan bahan-bahan (pisahkan dengan koma)", "")
    ingredients_list = [ingredient.strip() for ingredient in ingredients.split(",")]

    # Tombol untuk memanggil model AI dan menampilkan resep
    if st.button("Generate Resep"):
        if ingredients_list:
            resep = generate_resep(ingredients_list)
            st.subheader("Resep yang Dihasilkan:")
            st.write(resep)
        else:
            st.warning("Masukkan setidaknya satu bahan untuk menghasilkan resep.")

if __name__ == "__main__":
    main()
