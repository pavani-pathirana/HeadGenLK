import streamlit as st

TONE_OPTIONS = [
    "Standard (සාමාන්‍ය)",
    "Formal (රාජ්‍ය)",
    "Clickbait (ආකර්ෂණීය)",
]


def render() -> dict:
    """
    Render the sidebar and return the current user settings as a dict.

    Returns
    -------
    {
        "tone":           str,
        "num_candidates": int,
        "creativity":     float,
    }
    """
    with st.sidebar:
        st.markdown("""
            <div style="text-align:center; padding:1.5rem 0;">
                <h2 style="background:linear-gradient(135deg,#60a5fa,#a78bfa);
                           -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                           margin-top:0.5rem;">HeadGenLK</h2>
                <p style="font-size:0.8rem; color:#94a3b8;">Sinhala Headline Generator</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("### Tone Settings")
        tone = st.radio("Target Tone", TONE_OPTIONS, index=0)

        st.markdown("---")

        st.markdown("### Advanced")
        num_candidates = st.slider("Number of Candidates", 1, 5, 3)
        creativity     = st.slider("Creativity Level", 0.0, 1.0, 0.7)

        st.markdown("---")

        st.info("""
        **HeadGenLK Features:**
        - TextRank (Extractive)
        - mBART (Abstractive)
        - Hybrid (Proposed)

        Real-time performance profiling
        Memory usage tracking
        """)

        st.markdown("---")

        st.markdown("### System Stats")
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Models", "3")
        with c2:
            st.metric("Accuracy", "92%")

    return {
        "tone":           tone,
        "num_candidates": num_candidates,
        "creativity":     creativity,
    }