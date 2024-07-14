import sys

def parse_args():
    if len(sys.argv) != 3:
        print("Sposób użycia: python project.py inputFile outputFile")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    return input_file, output_file

if __name__ == "__main__":
    input_file, output_file = parse_args()
    print(f"Plik wejściowy: {input_file}")
    print(f"Plik wyjściowy: {output_file}")