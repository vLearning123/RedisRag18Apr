from src.vectorizer.tfidf_handler import create_tfidf_vectorizer
from src.vectorizer.vectorizer_store import save_vectorizer_to_redis_pickle, load_vectorizer_from_redis_pickle
from src.redis_store.store_vectors import store_document_vectors
from src.redis_store.index_creator import create_vector_index
from src.redis_store.search import search_similar_document


with open('data/corpus.txt', 'r',encoding='utf-8') as file:
    corpus = [line.strip() for line in file if line.strip()]

vectorizer = create_tfidf_vectorizer(corpus)
tfidf_matrix = vectorizer.transform(corpus)
save_vectorizer_to_redis_pickle(vectorizer)
store_document_vectors(tfidf_matrix, corpus)

vector_dim = tfidf_matrix.shape[1]
create_vector_index(index_name="doc_index", prefix="doc:", vector_dim=vector_dim)

print("TF-IDF vectorizer, document vectors and index have been saved to Redis.")

query_text = "audit opinion financial statements"

results = search_similar_document(query_text)

for score, content in results:
    print(f"Score: {score}, Content: {content}")