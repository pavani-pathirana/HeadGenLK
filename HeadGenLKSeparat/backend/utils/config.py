# Configuration & Constants for HeadGenLK

# API Configuration
GEMINI_API_KEY = "AIzaSyDWTTILZSaoewZ_sb-yin65ElD1wvh3z2Y"

# Model Paths
BASE_MODEL_PATH = "facebook/mbart-large-50"
ADAPTER_PATH = "./final_sinhala_mbart_lora_model/final_sinhala_mbart_lora_model"

# Model Parameters
MAX_INPUT_LENGTH = 800
MAX_OUTPUT_TOKENS = 64
BEAM_SIZE = 5

# TextRank Parameters
MIN_SENTENCE_LENGTH = 15
TEXTRANK_POSITION_BIAS = 0.15

# Style Prompts for Sinhala Headlines
STYLE_PROMPTS = {
    "Standard": "",
    "Trendy": "ට්‍රෙන්ඩි: ",
    "Serious": "බැරෑරුම්: ",
    "Short": "කෙටි: "
}

# UI Settings
GRADIENT_COLORS = ["#FF4B4B", "#FFD700", "#90EE90"]
