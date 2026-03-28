import streamlit as st


def inject():
    """Inject all custom CSS into the Streamlit page."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        * { font-family: 'Inter', sans-serif; }

        .stApp {
            background: linear-gradient(135deg, #0a0e1a 0%, #0f1422 50%, #0a0e1a 100%);
            background-attachment: fixed;
        }

        .main-container {
            background: rgba(18, 25, 45, 0.85);
            backdrop-filter: blur(12px);
            border-radius: 24px;
            padding: 2rem;
            margin: 1rem 0;
            border: 1px solid rgba(66, 153, 225, 0.2);
        }

        .gradient-text {
            background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 3.5rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0;
        }

        .modern-card {
            background: linear-gradient(135deg, rgba(30,41,59,0.9) 0%, rgba(15,23,42,0.95) 100%);
            border-radius: 20px;
            padding: 1.5rem;
            border: 1px solid rgba(96, 165, 250, 0.2);
            margin-bottom: 1rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }

        .modern-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border-color: rgba(96, 165, 250, 0.5);
        }

        .stats-card {
            background: rgba(15, 23, 42, 0.6);
            border-radius: 12px;
            padding: 12px;
            margin-top: 12px;
            border: 1px solid rgba(148, 163, 184, 0.2);
        }

        .model-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
            padding-bottom: 0.75rem;
            border-bottom: 2px solid rgba(96, 165, 250, 0.3);
        }

        .model-badge {
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.7rem;
            font-weight: 600;
            background: rgba(96, 165, 250, 0.2);
            color: #60a5fa;
            border: 1px solid rgba(96, 165, 250, 0.5);
        }

        .footer {
            text-align: center;
            padding: 2rem;
            background: rgba(15, 23, 42, 0.5);
            border-radius: 20px;
            margin-top: 2rem;
            border: 1px solid rgba(96, 165, 250, 0.2);
        }

        .stTextArea textarea {
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid rgba(96, 165, 250, 0.3);
            border-radius: 12px;
            color: #e2e8f0;
        }

        .stTextArea textarea:focus {
            border-color: #60a5fa;
            box-shadow: 0 0 0 3px rgba(96, 165, 250, 0.2);
        }

        .stButton button {
            background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(59, 130, 246, 0.4);
        }

        [data-testid="stMetricValue"] {
            font-size: 1.3rem;
            font-weight: 700;
            background: linear-gradient(135deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        [data-testid="stMetricLabel"] {
            color: #94a3b8;
            font-size: 0.8rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #0a0f1c 100%);
            border-right: 1px solid rgba(96, 165, 250, 0.2);
        }

        [data-testid="stSidebar"] * { color: #e2e8f0; }
        </style>
    """, unsafe_allow_html=True)