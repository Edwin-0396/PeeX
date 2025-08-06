import sys
import shutil
from pathlib import Path

# The goal is to perform a recursive file copy using a single function.
# By using shutil.copytree for a powerful, high-level abstraction.

if __name__ == "__main__":
    # Validate command-line arguments upfront for a clean user experience.
    if len(sys.argv) != 3:
        print("Usage: python script.py <source_path> <destination_path>", file=sys.stderr)
        sys.exit(1)

    try:
        # Use pathlib to create an object-oriented representation of the paths.
        source = Path(sys.argv[1])
        destination = Path(sys.argv[2])

        # This single line of code is the core of the automation.
        # It recursively copies the entire directory tree from source to destination.
        shutil.copytree(source, destination, dirs_exist_ok=True)
        print("Files copied successfully.")

    except Exception as e:
        # A single, catch-all exception handler is used for robustness.
        # It handles cases like a non-existent source, permission errors, etc.
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)