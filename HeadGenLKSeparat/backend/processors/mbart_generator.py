"""mBART-based abstractive headline generation module"""

import torch
from backend.utils.config import MAX_INPUT_LENGTH, MAX_OUTPUT_TOKENS, BEAM_SIZE


class MBartGenerator:
    """Abstractive headline generation using mBART + LoRA adapter"""
    
    def __init__(self, model_manager):
        """
        Initialize MBart generator
        
        Args:
            model_manager: ModelManager instance with loaded models
        """
        self.model = model_manager.get_model()
        self.tokenizer = model_manager.get_tokenizer()
        self.device = model_manager.get_device()
    
    def generate(self, text):
        """
        Generate headline using mBART
        
        Args:
            text (str): Input article text
        
        Returns:
            str: Generated headline
        """
        # Tokenize input
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            max_length=MAX_INPUT_LENGTH,
            truncation=True
        ).to(self.device)
        
        # Generate with beam search
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=MAX_OUTPUT_TOKENS,
                num_beams=BEAM_SIZE,
                no_repeat_ngram_size=2
            )
        
        # Decode output
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
