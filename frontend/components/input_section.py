import streamlit as st


def render() -> tuple[str, bool]:
    """
    Render the article input area and generate button.

    Returns
    -------
    (article_text: str, generate_clicked: bool)
    """
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    input_col, info_col = st.columns([2, 1])

    with input_col:
        st.markdown("### Input Article")
        article_text = st.text_area(
            "",
            height=200,
            placeholder=(
                "මෙහි පුවත් ලිපිය ඇතුළත් කරන්න...\n\n"
                "Paste your Sinhala news article here...\n\n"
                "Example: කොළඹ නගරයේ වාහන තදබදය අවම කිරීම සඳහා රජය නව පියවර ක්‍රියාත්මක කරයි..."
            ),
            label_visibility="collapsed",
        )

        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            generate_clicked = st.button(
                " Generate Headlines",
                use_container_width=True,
                type="primary",
            )

    with info_col:
        st.markdown("""
            <div style="background:linear-gradient(135deg,rgba(59,130,246,0.1),rgba(139,92,246,0.1));
                        padding:1.2rem; border-radius:16px; border:1px solid rgba(96,165,250,0.3);">
                <h4 style="color:#60a5fa; margin-top:0;">Performance Metrics</h4>
                <ul style="font-size:0.8rem; margin-bottom:0;">
                    <li>Inference Time (seconds)</li>
                    <li>Memory Usage (MB)</li>
                    <li>Model Comparison</li>
                    <li>Confidence Scores</li>
                </ul>
                <hr style="margin:0.8rem 0; border-color:rgba(96,165,250,0.2);">
                <p style="font-size:0.75rem; margin-bottom:0;">
                    Research Feature: Computational profiling for deployment feasibility analysis
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    return article_text, generate_clicked