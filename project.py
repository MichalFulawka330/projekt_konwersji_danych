import sys
import json
import xml.etree.ElementTree as ET
import yaml

def read_input(filename):
    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            return json.load(f)
    elif filename.endswith('.xml'):
        tree = ET.parse(filename)
        return {elem.tag: elem.text for elem in tree.iter()}
    elif filename.endswith('.yml') or filename.endswith('.yaml'):
        with open(filename, 'r') as f:
            return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported file format!")

def write_output(data, filename):
    if filename.endswith('.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    elif filename.endswith('.xml'):
        root = ET.Element("root")
        for key, val in data.items():
            elem = ET.SubElement(root, key)
            elem.text = str(val)
        tree = ET.ElementTree(root)
        tree.write(filename)
    elif filename.endswith('.yml') or filename.endswith('.yaml'):
        with open(filename, 'r') as f:
            yaml.dump(data, f)
    else:
        raise ValueError("Unsupported file format!")

def main():
    if len(sys.argv) != 3:
        print("Usage: python project.py inputFile outputFile")
        sys.exit(1)
    input_file, output_file = sys.argv[1], sys.argv[2]
    data = read_input(input_file)
    write_output(data, output_file)

if __name__ == "__main__":
    main()
