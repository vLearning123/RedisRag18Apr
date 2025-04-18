import numpy as np
from src.config.redis_client import get_redis_client


def store_document_vectors(tfidf_matrix,documents):
    """
    Store document vectors in Redis.
    """
    redis_client = get_redis_client()
    for i, doc_vector in enumerate(tfidf_matrix):
        doc_id = f"doc:{i}"
        vector_dense = doc_vector.toarray()[0].astype(np.float32)
        vector_bytes = vector_dense.tobytes()
        redis_client.hset(doc_id, mapping={
            "content": documents[i],
            "vector": vector_bytes
        })