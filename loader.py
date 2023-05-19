import json

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            return json_data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
