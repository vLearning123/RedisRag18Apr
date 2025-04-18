# import json
# import numpy as np
# from src.config.redis_client import get_redis_client
# from sklearn.feature_extraction.text import TfidfVectorizer


# def save_vectorizer_to_redis(vectorizer, vectorizer_key= "tfidf_vectorizer"):
#     """
#     Save the vectorizer to Redis.
#     """
#     redis_client = get_redis_client()
#     vectorizer_data = {
#         'vocabulary': vectorizer.vocabulary_,
#         'idf': vectorizer.idf_.tolist()
#     }
#     redis_client.set(vectorizer_key, json.dumps(vectorizer_data))

# def load_vectorizer_from_redis(key= "tfidf_vectorizer"):
  
#     redis_client = get_redis_client()
#     key = "tfidf_vectorizer"
#     data_bytes = redis_client.get(key)
#     if data_bytes is None:
#         raise ValueError(f"No data found in Redis for key: {key}")
#     data_str = data_bytes.decode('utf-8')
#     data = json.loads(data_str)
#     vectorizer = TfidfVectorizer()
#     vectorizer.vocabulary_ = data['vocabulary']
#     vectorizer.idf_ = data['idf']
#     return vectorizer

# src/vectorizer/vectorizer_store.py

# src/vectorizer/vectorizer_store.py

import io
import joblib
from src.config.redis_client import get_redis_client

def save_vectorizer_to_redis_pickle(vectorizer, key="tfidf_vectorizer:pkl"):
    """
    Serialize the fitted TF-IDF vectorizer into bytes via a BytesIO buffer,
    and store it in Redis under `key`.
    """
    r = get_redis_client()
    buffer = io.BytesIO()
    # Dump the vectorizer into the buffer
    joblib.dump(vectorizer, buffer)  # supports file-like objects :contentReference[oaicite:0]{index=0}
    buffer.seek(0)
    r.set(key, buffer.getvalue())

def load_vectorizer_from_redis_pickle(key="tfidf_vectorizer:pkl"):
    """
    Retrieve the pickled vectorizer bytes from Redis, wrap in BytesIO,
    and load the TF-IDF vectorizer object.
    """
    r = get_redis_client()
    blob = r.get(key)
    if blob is None:
        return None
    buffer = io.BytesIO(blob)
    buffer.seek(0)
    vectorizer = joblib.load(buffer)     # file-like load :contentReference[oaicite:1]{index=1}
    return vectorizer

