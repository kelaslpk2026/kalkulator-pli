import streamlit as st



def page_2():
    st.title("Page 2")

pg = st.navigation(["page_1.py", page_2])
pg.run()

st.title("🎈 Kalkulator PLI")
st.header(
    "Menghitung hasil operasi aritmatika sederhana", divider=True
)
number1 = st.number_input("Masukkan angka 1")
number2 = st.number_input("Masukkan angka 2")
