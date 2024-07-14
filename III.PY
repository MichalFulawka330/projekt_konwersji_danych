def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Dane zapisane do {filename}")
