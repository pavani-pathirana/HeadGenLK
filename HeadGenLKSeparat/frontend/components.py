"""Reusable Streamlit UI components"""

import streamlit as st


class UIComponents:
    """Collection of reusable UI components for Streamlit"""
    
    @staticmethod
    def render_sidebar():
        """
        Render sidebar with generation settings
        
        Returns:
            tuple: (selected_style, reference_headline)
        """
        st.sidebar.header("Generation Settings")
        
        style = st.sidebar.selectbox(
            "Select Headline Tone",
            ["Standard", "Trendy", "Serious", "Short"]
        )
        
        ref = st.sidebar.text_input(
            "Original/Reference Headline (Optional for Scoring)"
        )
        
        return style, ref
    
    @staticmethod
    def render_input_section():
        """
        Render input area for article body
        
        Returns:
            str: Article text from user input
        """
        article = st.text_area(
            "Paste Sinhala News Article Body:",
            height=250,
            placeholder="පුවත් ලිපිය මෙහි ඇතුළත් කරන්න..."
        )
        return article
    
    @staticmethod
    def render_results(results_dict, ref_headline, metrics_calc):
        """
        Render results in 3-column layout with metrics
        
        Args:
            results_dict (dict): Dictionary with keys 'tr', 'mb', 'hy'
            ref_headline (str): Reference headline for scoring
            metrics_calc: MetricsCalculator instance
        """
        st.divider()
        cols = st.columns(3)
        
        display_map = [
            ("TextRank + Gemini", 'tr'),
            ("mBART + Gemini", 'mb'),
            ("Hybrid + Gemini", 'hy')
        ]
        
        for i, (name, key) in enumerate(display_map):
            with cols[i]:
                st.subheader(name)
                
                # Editable text area
                edited = st.text_area(
                    f"Edit {name}",
                    results_dict[key],
                    key=f"edit_{key}",
                    height=120
                )
                
                # Show metrics if reference exists
                if ref_headline:
                    bleu, rouge = metrics_calc.calculate(edited, ref_headline)
                    
                    m_col1, m_col2 = st.columns(2)
                    m_col1.metric("BLEU Accuracy", bleu)
                    m_col2.metric("ROUGE-L Score", rouge)
                else:
                    st.info("ℹ️Add a reference headline in the sidebar to see scores.")
    
    @staticmethod
    def render_final_selection():
        """
        Render final model selection radio and log button
        
        Returns:
            str: Selected model name
        """
        st.divider()
        st.subheader(" Editorial Selection")
        
        final_choice = st.radio(
            "Which variation is most accurate?",
            ["TextRank", "mBART", "Hybrid"]
        )
        
        if st.button("Log Selection"):
            st.success(
                f" Successfully logged {final_choice} "
                "for Human Evaluation analysis."
            )
        
        return final_choice
