import streamlit as st
from PIL import Image
import codecs
import streamlit.components.v1 as components

#page navigations
Welcome = st.Page("Welcome.py", title="Welcome", icon="🌝")
About = st.Page("About.py", title="About", icon="⚽️")
Explore = st.Page("Explore.py", title="Explore", icon="📈")
Remarks = st.Page("Remarks.py", title="Remarks", icon="🎬")

page = st.navigation([Welcome,About,Explore,Remarks])
page.run()