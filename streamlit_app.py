import streamlit as st

st.title("🎈 Kalkulator PLI")
st.header(
    "Menghitung hasil operasi aritmatika sederhana", divider=True
)
number1 = st.number_input("Masukkan angka 1")
number2 = st.number_input("Masukkan angka 2")
if st.button("tambah"):
    st.header(number1+number2)

