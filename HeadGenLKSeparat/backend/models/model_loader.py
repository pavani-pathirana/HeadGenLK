"""Model loading and caching module for mBART + LoRA"""

import streamlit as st
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from peft import PeftModel
from backend.utils.config import (
    BASE_MODEL_PATH,
    ADAPTER_PATH,
    HF_TOKEN,
)


@st.cache_resource
def load_models():
    """Load and cache mBART base model with LoRA adapter"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if device == "cuda" else torch.float32
    
    # Load tokenizer
    tokenizer = MBart50TokenizerFast.from_pretrained(BASE_MODEL_PATH)
    tokenizer.src_lang = "si_LK"
    tokenizer.tgt_lang = "si_LK"
    
    # Load base model
    base_model = MBartForConditionalGeneration.from_pretrained(
        BASE_MODEL_PATH, torch_dtype=torch_dtype
    )
    
    # Load LoRA adapter
    model = PeftModel.from_pretrained(
    base_model,
    ADAPTER_PATH,
    token=HF_TOKEN,
)
    model = model.to(device)
    model.eval()
    
    return model, tokenizer, device


class ModelManager:
    """Manages model instances and device allocation"""
    
    def __init__(self):
        """Initialize ModelManager with cached models"""
        self.model, self.tokenizer, self.device = load_models()
    
    def get_model(self):
        """Get the mBART model"""
        return self.model
    
    def get_tokenizer(self):
        """Get the tokenizer"""
        return self.tokenizer
    
    def get_device(self):
        """Get the device (cuda or cpu)"""
        return self.device
