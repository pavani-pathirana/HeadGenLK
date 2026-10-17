import streamlit as st
from backend.models.model_loader import ModelManager
from backend.processors.textrank import TextRankProcessor
from backend.processors.mbart_generator import MBartGenerator
from backend.processors.tone_refiner import ToneRefiner
from backend.evaluators.metrics import MetricsCalculator
from frontend.components import UIComponents

# Service Initialization
 
@st.cache_resource
def init_services():
    """Initialize and cache all services"""
    return {
        'model_mgr': ModelManager(),
        'textrank': TextRankProcessor(),
        'tone_refiner': ToneRefiner(),
        'metrics': MetricsCalculator()
    }

# Main Application
def main():
    """Main Streamlit application"""
    
    # Page configuration
    st.set_page_config(
        page_title="Sinhala Headline Gen",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # # Title
    # st.title(" Sinhala News Headline Generation System")
    # st.markdown("---")
    
    # Initialize services
    services = init_services()
    model_mgr = services['model_mgr']
    textrank = services['textrank']
    tone_refiner = services['tone_refiner']
    metrics_calc = services['metrics']
    
    # Render UI components
    selected_style, ref_headline = UIComponents.render_sidebar()
    article_body = UIComponents.render_input_section()
         
    # Generation Pipeline
         
    if st.button("Generate Headlines "):
        if article_body:
            with st.spinner("Local mBART generating + Gemini Flash refining..."):
                try:
                    # Initialize generator
                    mbart_gen = MBartGenerator(model_mgr)
                    
                    # Step 1: Generate base headlines
                    st.info(" Step 1: Generating base headlines...")
                    tr_base = textrank.extract(article_body)
                    mb_base = mbart_gen.generate(article_body)
                    ext_context = textrank.extract(article_body, top_n=2)
                    hy_base = mbart_gen.generate(ext_context)
                    
                    # Step 2: Refine tone via Gemini
                    st.info(" Step 2: Refining tone with Gemini API...")
                    st.session_state['tr'] = tone_refiner.refine(tr_base, selected_style)
                    st.session_state['mb'] = tone_refiner.refine(mb_base, selected_style)
                    st.session_state['hy'] = tone_refiner.refine(hy_base, selected_style)
                    
                    st.success(" Generation complete!")
                    
                except Exception as e:
                    st.error(f" Error during generation: {str(e)}")
        else:
            st.warning(" Please enter an article body.")
    
    # Results Display
    if 'tr' in st.session_state:
        UIComponents.render_results(st.session_state, ref_headline, metrics_calc)
        UIComponents.render_final_selection()
         
    # Footer
         
    st.sidebar.markdown("---")
    st.sidebar.caption("BSc (Hons) in Computing - Final Year Research")


if __name__ == "__main__":
    main()
