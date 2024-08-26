import asyncio
from api_model import get_all_clients
import streamlit as st
import pandas as pd

if st.button('get_all_data'):
  data = asyncio.run(get_all_clients())
  df = pd.DataFrame(data)
  st.table(df)