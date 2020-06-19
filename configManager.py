import json

def load():
    with open('config.json') as f:
        config = json.load(f)
    return config
