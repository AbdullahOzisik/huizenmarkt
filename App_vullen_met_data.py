import streamlit as st
import pandas as pd

st.title("Woningprijzen per Provincie")

# Simpele voorbeeld data (later jouw echte data)
data = {
    'Provincie': ['Noord-Holland', 'Zuid-Holland', 'Utrecht'],
    'Gemiddelde Verkoopprijs': [350000, 320000, 360000],
    'Aantal Verkochte Woningen': [5000, 4800, 2100]
}
df = pd.DataFrame(data)

st.dataframe(df)
