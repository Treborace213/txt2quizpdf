import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_input_txt>")
        sys.exit(1)

    input_path = sys.argv[1]
    target_path = os.path.normpath(os.path.expandvars(os.path.expanduser(input_path)))

    if not os.path.isfile(target_path):
        print(f"Error: File does not exist -> {target_path}")
        sys.exit(1)

    print(f"Input file path: {target_path}")

if __name__ == "__main__":
    main()