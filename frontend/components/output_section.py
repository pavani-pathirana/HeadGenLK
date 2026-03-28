# frontend/components/output_section.py
from datetime import datetime

import pandas as pd
import streamlit as st

from components.charts import create_gauge, create_performance_bar

# Maps backend model_id → display metadata used only in the frontend
MODEL_DISPLAY = {
    "textrank": {"name": "Extractive (TextRank)", "badge": "Extractive", "icon": "", "color": "#3b82f6", "description": "Graph-based extraction • Fast & Efficient"},
    "mbart":    {"name": "Abstractive (mBART)",   "badge": "Abstractive", "icon": "", "color": "#8b5cf6", "description": "Neural generation • Creative & Natural"},
    "hybrid":   {"name": "Hybrid (HeadGenLK Pro)","badge": "Hybrid",      "icon": "",  "color": "#10b981", "description": "Combined approach • Best Balance"},
}


def render(results: list[dict], tone: str, creativity: float) -> None:
    """
    Render the full output section: performance chart, result cards, export.

    Parameters
    ----------
    results    : List of ModelResult dicts from the backend response.
    tone       : Selected tone string (for export metadata).
    creativity : Selected creativity value (for export metadata).
    """
    st.markdown('<div class="main-container">', unsafe_allow_html=True)

    #     Performance bar chart                                                                         ─
    st.markdown("### Model Performance Comparison")
    chart_data = [
        {
            "name":            MODEL_DISPLAY[r["model_id"]]["name"],
            "inference_time_s": r["inference_time_s"],
            "color":           MODEL_DISPLAY[r["model_id"]]["color"],
        }
        for r in results
    ]
    st.plotly_chart(create_performance_bar(chart_data), use_container_width=True)

    st.markdown("---")
    st.markdown("### Generated Headlines")
    st.markdown("*Edit and validate each headline to provide feedback*")
    st.markdown("---")

    #     Result cards    
    cols = st.columns(len(results))

    for idx, item in enumerate(results):
        meta = MODEL_DISPLAY[item["model_id"]]

        with cols[idx]:
            st.markdown(f"""
                <div class="modern-card">
                    <div class="model-header">
                        <span style="font-weight:700; color:#e2e8f0; font-size:1.1rem;">
                            {meta['icon']} {meta['name']}
                        </span>
                        <div class="model-badge">{meta['badge']}</div>
                    </div>
                    <p style="font-size:0.7rem; color:#94a3b8; margin-top:-0.5rem;">
                        {meta['description']}
                    </p>
            """, unsafe_allow_html=True)

            edited = st.text_area(
                "Edit Headline",
                value=item["headline"],
                key=f"edit_{idx}",
                height=80,
                label_visibility="collapsed",
            )

            st.markdown('<div class="stats-card">', unsafe_allow_html=True)
            st.plotly_chart(
                create_gauge(item["memory_delta_mb"], "Memory Usage", meta["color"]),
                use_container_width=True,
            )

            c1, c2, c3 = st.columns(3)
            with c1: st.metric("Time",       f"{item['inference_time_s']}s")
            with c2: st.metric("Memory",     f"{item['memory_delta_mb']:.1f} MB")
            with c3: st.metric("Confidence", f"{item['confidence']}%")
            st.markdown('</div>', unsafe_allow_html=True)

            if st.button(f"✓ Validate {meta['badge']}", key=f"validate_{idx}", use_container_width=True):
                original_words = set(item["headline"].split())
                edited_words   = set(edited.split())
                similarity     = len(original_words & edited_words) / max(len(original_words), 1)
                alignment      = int(item["confidence"] * (0.7 + similarity * 0.3)) if edited != item["headline"] else item["confidence"]
                alignment      = min(99, max(65, alignment))

                st.metric("Human Alignment Score", f"{alignment}%")
                if alignment > 90:
                    st.success("Excellent headline quality!")
                    st.balloons()
                elif alignment > 75:
                    st.success("Good headline — minor improvements made")
                else:
                    st.warning("Consider revising for better quality")

            st.markdown('</div>', unsafe_allow_html=True)

    #     Export             
    st.markdown("---")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        if st.button("Export Results & Performance Data", use_container_width=True):
            export_rows = []
            for idx, item in enumerate(results):
                meta = MODEL_DISPLAY[item["model_id"]]
                export_rows.append({
                    "Model":               meta["name"],
                    "Model_Type":          meta["badge"],
                    "Generated_Headline":  item["headline"],
                    "Edited_Headline":     st.session_state.get(f"edit_{idx}", item["headline"]),
                    "Inference_Time_s":    item["inference_time_s"],
                    "Memory_Usage_MB":     item["memory_delta_mb"],
                    "Confidence_Score":    item["confidence"],
                    "Tone":                tone,
                    "Creativity_Level":    creativity,
                    "Timestamp":           datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                })

            csv = pd.DataFrame(export_rows).to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"headgenlk_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True,
            )
            st.success("Data exported successfully!")

    st.markdown('</div>', unsafe_allow_html=True)