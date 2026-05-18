import streamlit as st

st.title("🎈 Kalkulator PLI")
st.header(
    "Menghitung hasil operasi aritmatika sederhana", divider=True
)
number1 = st.number_input("Masukkan angka 1")
number2 = st.number_input("Masukkan angka 2")
st.button("+"), st.button("-"),  st.button("x")= st.columns(3)
st.button(":"), st.button("^"), st.button("reset")=st.columns(3)
if st.button("+"):
    st.header(number1+number2)
elif st.button("-"):
    st.header(number1-number2)
elif st.button("x"):
    st.header(number1*number2)
elif st.button(":"):
    st.header(number1/number2)
elif st.button("^"):
    st.header(number1**number2)
elif st.button("reset"):
    st.rerun()
