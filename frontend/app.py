# frontend/app.py

from datetime import datetime

import streamlit as st

import styles
from api_client import generate_headlines
from components import sidebar, input_section, output_section

#Page config                                                               ─
st.set_page_config(
    page_title="HeadGenLK - Sinhala Headline Generator",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Styles  
styles.inject()

# Sidebar                                                                   ─
settings = sidebar.render()

# Header  
st.markdown("""
    <div style="text-align:center; padding:1rem 0 2rem 0;">
        <h1 class="gradient-text">HeadGenLK</h1>
        <p style="color:#94a3b8; margin-top:0.5rem;">
            AI-Powered Sinhala Headline Generation |
            Real-time Performance Profiling
        </p>
    </div>
""", unsafe_allow_html=True)

#    Input  ─
article_text, generate_clicked = input_section.render()

# Generate                                                                   
if generate_clicked:
    if not article_text.strip():
        st.error("කරුණාකර පුවත් ලිපියක් ඇතුළත් කරන්න / Please provide an article body first!")
    else:
        with st.spinner("Generating headlines…"):
            try:
                results = generate_headlines(
                    article    = article_text,
                    creativity = settings["creativity"],
                    tone       = settings["tone"],
                )
                st.session_state["gen_data"] = results
            except RuntimeError as e:
                st.error(str(e))

# Output  
if "gen_data" in st.session_state:
    output_section.render(
        results    = st.session_state["gen_data"],
        tone       = settings["tone"],
        creativity = settings["creativity"],
    )

#Footer  
st.markdown(f"""
    <div class="footer">
        <p>HeadGenLK | Sinhala Headline Generation System</p>
        <p style="font-size:0.8rem;">
            Powered by TextRank • mBART • Hybrid Models | Real-time Performance Profiling
        </p>
        <p style="font-size:0.7rem; color:#64748b;">
            Academic Research Project — Computational Feasibility Analysis | {datetime.now().year}
        </p>
    </div>
""", unsafe_allow_html=True)