"""UI"""

import streamlit as st


class UIComponents:
    """Collection of high-end, modern UI components for Streamlit"""

    @staticmethod
    def apply_streamlit_theme():
        """Apply theme programmatically directly inside Streamlit"""
        st.config.set_option("theme.base", "dark")
        st.config.set_option("theme.primaryColor", "#10B981")
        st.config.set_option("theme.backgroundColor", "#0B0D10")
        st.config.set_option("theme.secondaryBackgroundColor", "#11141B")
        st.config.set_option("theme.textColor", "#E2E8F0")

    @staticmethod
    def inject_custom_css():
        """Inject InfoPulse-inspired dark cinematic theme CSS"""
        UIComponents.apply_streamlit_theme()

        st.markdown(
            """
            <style>
            /* Global Background & Typography Setup */
            .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
                background-color: #0B0D10 !important;
                color: #E2E8F0 !important;
                font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
            }

            /* Hide Default Streamlit Chrome for Clean Look */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            /* Sidebar Styling Overrides */
            [data-testid="stSidebar"] {
                background-color: #11141B !important;
                border-right: 1px solid rgba(16, 185, 129, 0.15) !important;
            }

            /* Cinematic Hero Banner */
            .hero-banner {
                position: relative;
                width: 100%;
                padding: 35px 30px;
                border-radius: 20px;
                background: linear-gradient(180deg, rgba(16, 185, 129, 0.15) 0%, rgba(17, 24, 39, 0.8) 100%),
                            radial-gradient(circle at 50% -20%, rgba(16, 185, 129, 0.35), transparent 70%);
                border: 1px solid rgba(16, 185, 129, 0.25);
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.1);
                margin-bottom: 25px;
                overflow: hidden;
            }

            .hero-title {
                font-size: 2.2rem;
                font-weight: 800;
                color: #FFFFFF;
                margin-bottom: 8px;
                letter-spacing: -0.5px;
                line-height: 1.2;
            }

            .hero-subtitle {
                font-size: 0.95rem;
                color: #94A3B8;
                max-width: 650px;
            }

            /* InfoPulse Neon Pill Badges */
            .neon-pill {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                font-size: 0.72rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.8px;
                margin-bottom: 12px;
            }
            .pill-emerald {
                background: rgba(16, 185, 129, 0.15);
                color: #34D399;
                border: 1px solid rgba(16, 185, 129, 0.4);
            }
            .pill-purple {
                background: rgba(168, 85, 247, 0.15);
                color: #C084FC;
                border: 1px solid rgba(168, 85, 247, 0.4);
            }

            /* Section Headers with SVG Glow Icons */
            .section-header {
                display: flex;
                align-items: center;
                gap: 10px;
                font-size: 1.1rem;
                font-weight: 700;
                color: #F8FAFC !important;
                letter-spacing: 0.2px;
                margin-bottom: 14px;
            }
            .section-header svg {
                width: 20px;
                height: 20px;
                fill: #10B981;
                filter: drop-shadow(0px 0px 6px rgba(16, 185, 129, 0.6));
            }

            /* Article Textarea & Input Card Overrides */
            textarea, input {
                background-color: #11141B !important;
                color: #E2E8F0 !important;
                border: 1px solid #222938 !important;
                border-radius: 12px !important;
                padding: 12px !important;
            }
            textarea:focus, input:focus {
                border-color: #10B981 !important;
                box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.2) !important;
            }

            /* Modern Floating Metric Cards */
            .metric-card {
                background: #11141B;
                border: 1px solid #222938;
                border-radius: 12px;
                padding: 12px;
                text-align: center;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                transition: transform 0.2s ease, border-color 0.2s ease;
            }
            .metric-card:hover {
                border-color: #10B981;
                transform: translateY(-2px);
            }
            .metric-title {
                font-size: 0.68rem;
                font-weight: 700;
                color: #64748B;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .metric-value {
                font-size: 1.35rem;
                font-weight: 800;
                color: #10B981;
                text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
            }

            /* Info Box Notice */
            .info-callout {
                font-size: 0.8rem;
                color: #64748B;
                background: rgba(17, 20, 27, 0.8);
                border-left: 3px solid #10B981;
                padding: 10px 12px;
                border-radius: 0 8px 8px 0;
                margin-top: 10px;
            }

            /* InfoPulse Style Action Buttons */
            div.stButton > button {
                background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
                color: #0B0D10 !important;
                font-weight: 700 !important;
                border: none !important;
                border-radius: 10px !important;
                padding: 0.6rem 1.2rem !important;
                box-shadow: 0 6px 20px rgba(16, 185, 129, 0.3) !important;
                transition: all 0.2s ease-in-out !important;
            }
            div.stButton > button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 25px rgba(16, 185, 129, 0.5) !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_hero_banner():
        """Render top InfoPulse style header banner with integrated description"""
        st.markdown(
            """
            <div class="hero-banner">
                <span class="neon-pill pill-emerald">AI Headlines Engine</span>
                <div class="hero-title">HeadGenLK Intelligence</div>
                <div class="hero-subtitle">Sinhala News Headline Generation System</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_sidebar():
        """Render sidebar with generation settings"""
        UIComponents.inject_custom_css()

        st.sidebar.markdown(
            """
            <div class="section-header">
                <svg viewBox="0 0 24 24"><path d="M3 17v2h6v-2H3M3 5v2h10V5H3m10 16v-2h8v-2h-8v-2h-2v6h2M7 9v2H3v2h4v2h2V9H7m14 4v-2H11v2h10m-6-8v2h6V7h-6z"/></svg>
                <span>Generation Settings</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        style = st.sidebar.selectbox(
            "Headline Tone",
            ["Standard", "Trendy", "Serious", "Short"],
            help="Choose the tone and style for the generated headline.",
        )

        ref = st.sidebar.text_input(
            "Reference Headline",
            placeholder="Ground truth headline for evaluation...",
            help="Optional: Input a human-written baseline to compute BLEU & ROUGE metrics.",
        )

        return style, ref

    @staticmethod
    def render_input_section():
        """Render input area for article body"""
        UIComponents.render_hero_banner()

        st.markdown(
            """
            <div class="section-header">
                <svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                <span>News Content Input</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        article = st.text_area(
            label="Article Text",
            label_visibility="collapsed",
            height=200,
            placeholder="පුවත් ලිපිය මෙහි ඇතුළත් කරන්න (Paste Sinhala news article body here)...",
        )
        return article

    @staticmethod
    def render_results(results_dict, ref_headline, metrics_calc):
        """Render results in 3-column layout with metrics"""
        st.divider()

        st.markdown(
            """
            <div class="section-header">
                <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
                <span>Generated Headline Candidates</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        cols = st.columns(3)

        display_map = [
            ("TextRank + Gemini", "tr"),
            ("mBART + Gemini", "mb"),
            ("Hybrid + Gemini", "hy"),
        ]

        for i, (name, key) in enumerate(display_map):
            with cols[i]:
                st.markdown(f'<span class="neon-pill pill-purple">Strategy 0{i+1}</span>', unsafe_allow_html=True)
                st.subheader(name)

                # Editable text area
                edited = st.text_area(
                    f"Edit Output",
                    results_dict[key],
                    key=f"edit_{key}",
                    height=120,
                    label_visibility="collapsed",
                )

                # Show metrics if reference exists
                if ref_headline:
                    bleu, rouge = metrics_calc.calculate(edited, ref_headline)

                    m_col1, m_col2 = st.columns(2)
                    with m_col1:
                        st.markdown(
                            f"""
                            <div class="metric-card">
                                <div class="metric-title">BLEU</div>
                                <div class="metric-value">{bleu}</div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                    with m_col2:
                        st.markdown(
                            f"""
                            <div class="metric-card">
                                <div class="metric-title">ROUGE-L</div>
                                <div class="metric-value">{rouge}</div>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.markdown(
                        """
                        <div class="info-callout">
                            Enter a reference headline in sidebar to reveal BLEU & ROUGE accuracy scores.
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    @staticmethod
    def render_final_selection():
        """render final model selection radio and log button"""
        st.divider()

        st.markdown(
            """
            <div class="section-header">
                <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span>Human Evaluation & Logging</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        col1, col2 = st.columns([2, 1])

        with col1:
            final_choice = st.radio(
                "Select candidate variation with optimal accuracy:",
                ["TextRank", "mBART", "Hybrid"],
                horizontal=True,
            )

        with col2:
            st.write(" ")
            st.write(" ")
            if st.button("Log Selection", use_container_width=True):
                st.toast(f"Assessment logged: {final_choice}", icon="")
                st.success(f"Logged {final_choice} for evaluation.")

        return final_choice