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
            gemini_model = genai.GenerativeModel("gemini-2.5-flash")
            prompt = self._build_prompt(headline, tone)
            response = gemini_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            st.error(f"Gemini API Error: {e}")
            return headline
    
    @staticmethod
    def _build_prompt(headline, tone):
        """Build prompt for Gemini API"""
        return f"""
You are a professional Sinhala news editor.
Convert the following Sinhala news headline into a '{tone}' style.
- Keep the core meaning exactly the same.
- Output ONLY the converted headline in Sinhala.
- Do not add any English text or explanations.

Original Headline: {headline}
{tone} Headline:"""
