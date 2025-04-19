import numpy as np
from redis.commands.search.query import Query
from src.config.redis_client import get_redis_client
from src.vectorizer.vectorizer_store import load_vectorizer_from_redis_pickle

def search_similar_document(query_text: str, top_k: int = 3):
    """
    Search for the most similar documents to the query text using Redis.
    """
    # Load the vectorizer from Redis
    vectorizer = load_vectorizer_from_redis_pickle()
    if vectorizer is None:
        raise ValueError("Vectorizer not found in Redis. Please ensure it is saved before searching.")

    # Transform the query into a TF-IDF vector
    query_vector_sparse = vectorizer.transform([query_text])

    # Convert the sparse matrix to a dense array
    query_vector_dense = query_vector_sparse.toarray()

    # Ensure the dense array has the correct shape and type
    query_vector = query_vector_dense[0].astype(np.float32)

    # Convert the vector to bytes for Redis
    query_vector_bytes = query_vector.tobytes()

    # Connect to Redis
    redis_client = get_redis_client()

    # Define the search query
    redis_query = (
        Query(f"*=>[KNN {top_k} @vector $query_vector_bytes AS score]")
        .sort_by("score")
        .return_fields("content", "score")
        .dialect(2)
    )

    # Execute the search
    results = redis_client.ft("doc_index").search(
        redis_query, query_params={"query_vector_bytes": query_vector_bytes}
    )

    # Extract and return the document scores and contents
    return [(doc.score, doc.content) for doc in results.docs]
