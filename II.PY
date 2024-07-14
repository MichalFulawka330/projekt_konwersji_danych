import json

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print("Prawidłowy plik JSON.")
        return data
    except json.JSONDecodeError:
        print("Nieprawidłowy plik JSON.")
        sys.exit(1)