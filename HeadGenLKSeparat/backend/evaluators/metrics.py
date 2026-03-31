"""Evaluation metrics module for headline assessment"""

import sacrebleu
from rouge_score import rouge_scorer


class MetricsCalculator:
    """Calculate BLEU and ROUGE-L scores for evaluation"""
    
    @staticmethod
    def calculate(generated, reference):
        """
        Calculate BLEU and ROUGE-L metrics
        
        Args:
            generated (str): Generated headline
            reference (str): Reference/ground truth headline
        
        Returns:
            tuple: (BLEU score, ROUGE-L score)
        """
        if not reference:
            return 0.0, 0.0
        
        # Calculate BLEU with floor smoothing for Sinhala text
        bleu = sacrebleu.sentence_bleu(
            generated,
            [reference],
            smooth_method='floor'
        ).score
        
        # Calculate ROUGE-L
        scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=False)
        rouge_l = scorer.score(reference, generated)['rougeL'].fmeasure
        
        return round(bleu, 2), round(rouge_l, 4)
