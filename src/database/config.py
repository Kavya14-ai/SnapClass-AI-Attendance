import streamlit as st

from supabase import create_client, Client

# Temporary debugging: check the loaded Supabase URL
st.write("URL:", repr(st.secrets["SUPABASE_URL"]))

# Connect to Supabase
supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)
