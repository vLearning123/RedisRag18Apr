from sklearn.feature_extraction.text import TfidfVectorizer

def create_tfidf_vectorizer(corpus):
    """
    Create a TF-IDF vectorizer and fit it to the provided corpus.

    Args:
        corpus (list of str): The text documents to be vectorized.

    Returns:
        TfidfVectorizer: The fitted TF-IDF vectorizer.
    """
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectorizer.fit(corpus)
    return tfidf_vectorizer
