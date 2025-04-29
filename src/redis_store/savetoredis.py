import json
import redis
from redis.commands.json.path import Path
from src.config import get_redis_client, clear_redis_database


def load_data_into_redis(client):
    """
    Load data from JSON files into Redis.
    """

    clear_redis_database(client)
    # Load child_par.json
    with open('data/child_par.json', 'r') as f:
        child_par_data = json.load(f)

    # Load node.json
    with open('data/node.json', 'r') as f:
        node_data = json.load(f)

    # Store each dictionary from child_par.json as a separate JSON document
    for idx, item in enumerate(child_par_data, start=1):
        key = f"cb:childpar:{idx}"
        client.json().set(key, Path.root_path(), item)

    # Store the entire node.json list as a single JSON array
    client.json().set("cb:nodes", Path.root_path(), node_data)


def retrieve_and_print_data(client):
    """
    Retrieve and print data from Redis.
    """
    # Retrieve and deserialize a specific childpar entry
    childpar_entry = json.loads(client.get(b"cb:childpar:1"))
    print(childpar_entry)

    # Retrieve and deserialize the entire nodes list
    nodes_list = json.loads(client.get("cb:nodes"))
    print(nodes_list)
