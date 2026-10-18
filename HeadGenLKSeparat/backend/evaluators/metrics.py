"""Evaluation metrics module for headline assessment"""

import sacrebleu
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


class WhitespaceTokenizer:
    """Tokenize Sinhala text without ASCII-specific word matching."""

    @staticmethod
    def tokenize(text):
        return text.split()


class MetricsCalculator:
    """Calculate BLEU and ROUGE scores for evaluation"""
    
    @staticmethod
    def calculate(generated, reference):
        if not reference:
            return {
                "rouge1": 0.0,
                "rouge2": 0.0,
                "rougeL": 0.0,
                "sacrebleu": 0.0,
                "nltk_bleu": 0.0,
            }

        generated_tokens = generated.split()
        reference_tokens = reference.split()

        scorer = rouge_scorer.RougeScorer(
            ["rouge1", "rouge2", "rougeL"],
            use_stemmer=False,
            tokenizer=WhitespaceTokenizer(),
        )
        rouge_scores = scorer.score(reference, generated)

        sacrebleu_score = sacrebleu.sentence_bleu(
            generated,
            [reference],
            tokenize="none",
            smooth_method="floor",
        ).score

        nltk_score = sentence_bleu(
            [reference_tokens],
            generated_tokens,
            weights=(0.25, 0.25, 0.25, 0.25),
            smoothing_function=SmoothingFunction().method1,
        ) 

        return {
            "rouge1": round(rouge_scores["rouge1"].fmeasure , 4),
            "rouge2": round(rouge_scores["rouge2"].fmeasure , 4),
            "rougeL": round(rouge_scores["rougeL"].fmeasure , 4),
            "sacrebleu": round(sacrebleu_score, 2),
            "nltk_bleu": round(nltk_score, 4),
        }
