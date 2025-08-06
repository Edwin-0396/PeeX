import sys
import shutil
from pathlib import Path

# The goal is to perform a recursive file copy without explicit loops or conditionals.
# We achieve this by leveraging the powerful, high-level abstraction of shutil.copytree.
# The `try...except` block is a crucial part of a robust, defensive script.
# It handles potential errors gracefully without the need for a traditional `if` statement.

try:
    # A robust script must handle user input. We get source and destination
    # paths from command-line arguments. This avoids hardcoding.
    # sys.argv is a list of command-line arguments, where sys.argv[0] is the script name.
    # We expect the user to provide two arguments: source and destination.
    source_path_str = sys.argv[1]
    destination_path_str = sys.argv[2]

    # The pathlib module provides an object-oriented interface for filesystem paths,
    # making the script OS-agnostic and more readable.
    source = Path(source_path_str)
    destination = Path(destination_path_str)

    # This single line of code is the entire core of the automation.
    # shutil.copytree() recursively copies the entire directory tree from source to destination.
    # It handles all the iteration, directory creation, and file copying internally.
    # The `dirs_exist_ok=True` parameter is a modern best practice, allowing the
    # copy to succeed even if the destination directory already exists.
    shutil.copytree(source, destination, dirs_exist_ok=True)

    # Output to the console. We provide a simple confirmation message
    # to avoid printing potentially sensitive paths and maintain a clean user experience.
    print("Files copied successfully.")

except IndexError:
    # This exception handles the case where the user did not provide
    # the required command-line arguments. It provides a clear, defensive error message.
    # We use sys.stderr for error output, which is a standard practice.
    print("Error: Missing required arguments. Please provide source and destination paths.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    # This is a generic exception handler for any other potential issues,
    # such as a non-existent source directory or permission errors.
    # It ensures the script fails gracefully.
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(1)
