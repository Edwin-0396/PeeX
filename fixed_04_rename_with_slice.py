import sys
from pathlib import Path

def rename_files(folder_path, file_type, slice_index):
    """
    Renames files in a folder by removing characters from the end of the filename.
    """
    try:
        path = Path(folder_path)
        for file in path.glob(f"*{file_type}"):
            if file.is_file():
                new_name = f"{file.stem[:slice_index]}{file.suffix}"
                file.rename(path / new_name)
                print(f"Renamed '{file.name}' to '{new_name}'")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python rename_script.py <folder_path> <file_type> <slice_index>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    file_type = sys.argv[2]
    
    try:
        slice_index = int(sys.argv[3])
    except ValueError:
        print("Error: The slice index must be an integer.", file=sys.stderr)
        sys.exit(1)
        
    rename_files(folder_path, file_type, slice_index)