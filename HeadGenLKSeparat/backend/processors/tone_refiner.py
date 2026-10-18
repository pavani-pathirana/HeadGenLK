"""Tone refinement module using Google Gemini API"""

import streamlit as st
import google.generativeai as genai
from backend.utils.config import GEMINI_API_KEY, STYLE_PROMPTS


class ToneRefiner:
    """Refine headline tone using Google Gemini 1.5 Flash API"""
    
    def __init__(self):
        """Initialize ToneRefiner with Gemini configuration"""
        genai.configure(api_key=GEMINI_API_KEY)
    
    def refine(self, headline, tone="Standard"):
        """
        Refine headline tone using Gemini API
        
        Args:
            headline (str): Original headline
            tone (str): Target tone (Standard, Trendy, Serious, Short)
        
        Returns:
            str: Refined headline or original if tone is Standard
        """
        if tone == "Standard":
            return headline
        
        try:
            gemini_model = genai.GenerativeModel("gemini-3.1-flash-lite")
            #gemini_model = genai.GenerativeModel("gemini-2.5-flash")
            prompt = self._build_prompt(headline, tone)
            response = gemini_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            st.error(f"Gemini API Error: {e}")
            return headline
    
    @staticmethod
    def _build_prompt(headline, tone):
        """Build a style-specific prompt for Gemini API"""
        style_instruction = STYLE_PROMPTS.get(
            tone,
            "Use clear and accurate Sinhala news language.",
        )

        return f"""
You are a professional Sinhala news editor.
Rewrite the following Sinhala news headline using this style:
Style: {tone}
Instruction: {style_instruction}

Rules:
- Keep the original facts and meaning unchanged.
- Output ONLY one Sinhala headline.
- Do not add explanations.
- Do not invent names, dates, locations, or events.
- Keep the headline concise.

Original headline:
{headline}

Rewritten headline:
"""
