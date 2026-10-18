import streamlit as st
# Configuration & Constants for HeadGenLK

# API Configuration
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

# Model Paths
BASE_MODEL_PATH = "facebook/mbart-large-50"
# ADAPTER_PATH = "./final_sinhala_mbart_lora_model/final_sinhala_mbart_lora_model"
HF_TOKEN = st.secrets["HF_TOKEN"]
ADAPTER_PATH = "pava0000/final_sinhala_mbart_lora_model"

# Model Parameters
MAX_INPUT_LENGTH = 800
MAX_OUTPUT_TOKENS = 64
BEAM_SIZE = 5

# TextRank Parameters
MIN_SENTENCE_LENGTH = 15
TEXTRANK_POSITION_BIAS = 0.15

# Style Prompts for Sinhala Headlines
STYLE_PROMPTS = {
    "Standard": "Keep the original neutral news style.",
    "Trendy": "Use modern, attention-grabbing wording while remaining accurate.",
    "Serious": "Use formal, objective, and authoritative wording.",
    "Short": "Make the headline very brief and concise.",
    "Breaking News": "Emphasize urgency and the most important immediate event.",
    "Neutral": "Use completely objective and unbiased news language.",
    "Political": "Use formal political-news wording and preserve political facts.",
    "Sports": "Use energetic sports-news language and highlight the event or result.",
    "Business": "Use professional business and economic-news language.",
    "Emotional": "Use emotionally engaging wording without exaggeration or false claims.",
    "Question": "Rewrite the headline as a clear and informative question.",
    "Social Media": "Use concise, engaging wording suitable for a news social-media post.",
}

# UI Settings
GRADIENT_COLORS = ["#FF4B4B", "#FFD700", "#90EE90"]
