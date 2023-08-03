# file_handling.py
import json

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

def write_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)
