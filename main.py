import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_input_txt>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.isfile(input_path):
        print(f"Error: File does not exist -> {input_path}")
        sys.exit(1)

    print(f"Input file path: {input_path}")

if __name__ == "__main__":
    main()