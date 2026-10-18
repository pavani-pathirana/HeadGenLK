"""UI"""

import csv
import io
from datetime import datetime, timezone

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
            [
                "Standard",
                "Trendy",
                "Serious",
                "Short",
                "Breaking News",
                "Neutral",
                "Political",
                "Sports",
                "Business",
                "Emotional",
                "Question",
                "Social Media",
            ],
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
    def render_metric_list(title, scores):
        metrics = [
            ("ROUGE-1", scores["rouge1"]),
            ("ROUGE-2", scores["rouge2"]),
            ("ROUGE-L", scores["rougeL"]),
            ("SacreBLEU", scores["sacrebleu"]),
            ("NLTK BLEU", scores["nltk_bleu"]),
        ]

        rows = "".join(
            f"""
            <div style="
                display:flex;
                justify-content:space-between;
                padding:8px 0;
                border-bottom:1px solid #222938;
            ">
                <span style="color:#94A3B8;">{label}</span>
                <strong style="color:#34D399;">{value:.2f}</strong>
            </div>
            """
            for label, value in metrics
        )

        st.markdown(
            f"""
            <div style="
                background:#11141B;
                border:1px solid #222938;
                border-radius:12px;
                padding:12px;
                margin-top:10px;
            ">
                <div style="
                    color:#F8FAFC;
                    font-weight:700;
                    margin-bottom:6px;
                ">
                    {title}
                </div>
                {rows}
            </div>
            """,
            unsafe_allow_html=True,
        )

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
            ("TextRank", "tr_base", "tr"),
            ("mBART", "mb_base", "mb"),
            ("Hybrid", "hy_base", "hy"),
        ]

        for i, (name, base_key, refined_key) in enumerate(display_map):
            with cols[i]:
                st.markdown(f'<span class="neon-pill pill-purple">Strategy 0{i+1}</span>', unsafe_allow_html=True)
                st.subheader(name)

                original = st.text_area(
                    "Original model headline",
                    results_dict[base_key],
                    key=f"original_{refined_key}",
                    height=100,
                )

                refined = st.text_area(
                    "Gemini-refined headline",
                    results_dict[refined_key],
                    key=f"refined_{refined_key}",
                    height=120,
                )

                if ref_headline:
                    original_scores = metrics_calc.calculate(original, ref_headline)
                    refined_scores = metrics_calc.calculate(refined, ref_headline)

                    UIComponents.render_metric_list("Original metrics", original_scores)
                    UIComponents.render_metric_list("Refined metrics", refined_scores)
                else:
                    st.markdown(
                        """
                        <div class="info-callout">
                            Enter a reference headline to reveal the metrics.
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    @staticmethod
    def render_human_evaluation(
        results_dict,
        selected_style,
        article_body,
        reference_headline,
    ):
        """Collect and persist ratings for all generated model headlines."""
        from backend.storage.evaluation_store import (
            get_evaluations,
            save_evaluations,
        )

        st.divider()

        st.markdown(
            """
            <div class="section-header">
                <svg viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                <span>Human Evaluation</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption("Rate all three model outputs using a 5-point Likert scale.")

        version = st.radio(
            "Headline version",
            ["Original model output", "Gemini-refined output"],
            horizontal=True,
        )

        rating_options = [1, 2, 3, 4, 5]
        rating_labels = {
            1: "1 - Very poor",
            2: "2 - Poor",
            3: "3 - Fair",
            4: "4 - Good",
            5: "5 - Excellent",
        }

        def rating_label(value):
            return rating_labels[value]

        models = [
            ("TextRank", "tr_base", "tr"),
            ("mBART", "mb_base", "mb"),
            ("Hybrid", "hy_base", "hy"),
        ]
        headline_version_key = 1 if version == "Gemini-refined output" else 0
        ratings = []

        with st.form("human_evaluation_form"):
            columns = st.columns(3)

            for column, (method, original_key, refined_key) in zip(columns, models):
                with column:
                    headline_key = (original_key, refined_key)[headline_version_key]
                    headline = st.text_area(
                        f"{method} headline",
                        results_dict[headline_key],
                        key=f"evaluation_headline_{method}",
                        height=100,
                    )
                    relevance = st.select_slider(
                        "Relevance",
                        options=rating_options,
                        value=3,
                        format_func=rating_label,
                        key=f"evaluation_relevance_{method}",
                    )
                    accuracy = st.select_slider(
                        "Accuracy",
                        options=rating_options,
                        value=3,
                        format_func=rating_label,
                        key=f"evaluation_accuracy_{method}",
                    )
                    readability = st.select_slider(
                        "Readability",
                        options=rating_options,
                        value=3,
                        format_func=rating_label,
                        key=f"evaluation_readability_{method}",
                    )
                    conciseness = st.select_slider(
                        "Conciseness",
                        options=rating_options,
                        value=3,
                        format_func=rating_label,
                        key=f"evaluation_conciseness_{method}",
                    )
                    ratings.append({
                        "method": method,
                        "version": version,
                        "headline": headline,
                        "relevance": relevance,
                        "accuracy": accuracy,
                        "readability": readability,
                        "conciseness": conciseness,
                    })

            submitted = st.form_submit_button(
                "Save All Evaluations",
                use_container_width=True,
            )

        if submitted:
            timestamp = datetime.now(timezone.utc).isoformat()
            records = []
            for rating in ratings:
                rating.update({
                    "timestamp_utc": timestamp,
                    "tone": selected_style,
                    "article": article_body,
                    "reference_headline": reference_headline,
                    "average_score": round(
                        (
                            rating["relevance"]
                            + rating["accuracy"]
                            + rating["readability"]
                            + rating["conciseness"]
                        ) / 4,
                        2,
                    ),
                })
                records.append(rating)

            try:
                save_evaluations(records)
                st.success("All three model evaluations were saved to MongoDB.")
            except Exception as error:
                st.error(f"Could not save evaluations: {error}")

        try:
            evaluations = get_evaluations()
        except Exception:
            evaluations = []

        if evaluations:
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=evaluations[0].keys())
            writer.writeheader()
            writer.writerows(evaluations)
            st.download_button(
                "Download Evaluations CSV",
                output.getvalue(),
                file_name="human_evaluations.csv",
                mime="text/csv",
                use_container_width=True,
            )
