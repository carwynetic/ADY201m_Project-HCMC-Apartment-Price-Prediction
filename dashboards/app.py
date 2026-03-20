import streamlit as st
from utils import load_data, apply_filters, create_kpis

st.set_page_config(page_title="HCMC Dashboard", layout="wide")
st.title("HCMC Apartment Dashboard")

df = load_data()
if df is None:
    st.error("Missing dataset")
    st.stop()

df = apply_filters(df)
kpis = create_kpis(df)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total", kpis["count"])
c2.metric("Avg Price/m2", kpis["avg_price"])
c3.metric("Median Price/m2", kpis["median_price"])
c4.metric("Avg Area", kpis["avg_area"])

st.dataframe(df.head())
