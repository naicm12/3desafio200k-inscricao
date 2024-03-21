import streamlit as st

st.markdown("#### Regulamento")
with open('Regulamento.txt','r',encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        st.write(line)


