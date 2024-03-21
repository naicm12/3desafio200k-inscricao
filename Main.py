import streamlit as st
import MySQLdb
import sqlalchemy
from streamlit.connections import SQLConnection

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from TESTE;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NOME}")
