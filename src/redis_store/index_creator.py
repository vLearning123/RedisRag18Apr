import redis
from redis.commands.search.field import VectorField, TextField
from redis.commands.search.indexDefinition import IndexType, IndexDefinition
from src.config.redis_client import get_redis_client

def create_vector_index(index_name: str, prefix: str, vector_dim: int):
    """
    Create a Redis index for storing document vectors and their content.
    """
    redis_client = get_redis_client()
    try:
        redis_client.ft(index_name).info()
        print(f"Index '{index_name}' already exists.")
    except redis.exceptions.ResponseError:

        schema = (
            TextField("content"),
            VectorField("vector", "FLAT", {
                "TYPE": "FLOAT32",
                "DIM": vector_dim,
                "DISTANCE_METRIC": "COSINE"
            })
        )

        redis_client.ft(index_name).create_index(
            fields = schema,
            definition=IndexDefinition(prefix=[prefix], index_type=IndexType.HASH)
        )

        print(f"Index '{index_name}' created successfully.")