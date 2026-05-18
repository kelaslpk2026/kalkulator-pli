import streamlit as st

st.title("🎈 Kalkulator PLI")
st.header(
    "Menghitung hasil operasi aritmatika sederhana", divider=True
)
number1 = st.number_input("Masukkan angka 1")
number2 = st.number_input("Masukkan angka 2")

tambah=st.button("+")
kurang=st.button("-")
kali=st.button("+")
bagi=st.button("-")
pangkat=st.button("+")
reset=st.button("reset")
tambah, kurang, kali=st.columns(3)
bagi, pangkat, reset=st.columns(3)
st.button("+"), st.button("-"),  st.button("x")= st.columns(3)
st.button(":"), st.button("^"), st.button("reset")=st.columns(3)
if tambah:
    st.header(number1+number2)
elif kurang:
    st.header(number1-number2)
elif kali:
    st.header(number1*number2)
elif bagi:
    st.header(number1/number2)
elif pangkat:
    st.header(number1**number2)
elif reset:
    st.rerun()
