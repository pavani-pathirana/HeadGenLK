"""TextRank-based extractive summarization module"""

import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from backend.utils.config import MIN_SENTENCE_LENGTH, TEXTRANK_POSITION_BIAS


class TextRankProcessor:
    """Extractive headline generation using TextRank algorithm"""
    
    def __init__(self):
        """Initialize TextRank processor with config parameters"""
        self.min_length = MIN_SENTENCE_LENGTH
        self.position_bias = TEXTRANK_POSITION_BIAS
    
    def extract(self, text, top_n=1):
        """
        Extract top-N sentences using TextRank algorithm
        
        Args:
            text (str): Input article text
            top_n (int): Number of sentences to extract
        
        Returns:
            str: Extracted headline(s)
        """
        # Split into sentences
        sentences = [s.strip() for s in text.split('.') 
                     if len(s.strip()) > self.min_length]
        
        # If not enough sentences, return original text
        if len(sentences) <= top_n:
            return text
        
        # Calculate TF-IDF matrix
        tv = TfidfVectorizer()
        tfidf_matrix = tv.fit_transform(sentences)
        
        # Calculate cosine similarity
        sim_matrix = cosine_similarity(tfidf_matrix)
        
        # Build graph and run PageRank
        nx_graph = nx.from_numpy_array(sim_matrix)
        scores = nx.pagerank(nx_graph)
        
        # Add position bias (important info usually at start)
        for i in range(len(scores)):
            scores[i] += self.position_bias * (1 - i / len(scores))
        
        # Rank sentences and select top-N
        ranked = sorted(
            ((scores[i], s) for i, s in enumerate(sentences)), 
            reverse=True
        )
        
        return ". ".join([ranked[i][1] for i in range(min(top_n, len(ranked)))])
