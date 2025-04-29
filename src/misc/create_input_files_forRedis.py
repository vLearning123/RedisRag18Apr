import json

# Define the data for child_par.json: a list of dictionaries
child_par_data = [
    {"id": 1, "name": "Node A"},
    {"id": 2, "name": "Node B"},
    {"id": 3, "name": "Node C"},
    {"id": 4, "name": "Node D"},
    {"id": 5, "name": "Node E"}
]

# Extract the 'name' values for node.json
node_data = [item["name"] for item in child_par_data]

# Write child_par_data to child_par.json
with open('child_par.json', 'w') as cp_file:
    json.dump(child_par_data, cp_file, indent=4)

# Write node_data to node.json
with open('node.json', 'w') as node_file:
    json.dump(node_data, node_file, indent=4)
