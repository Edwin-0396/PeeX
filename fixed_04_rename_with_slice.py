import sys
from pathlib import Path

def rename_files(folder_path, file_type, slice_index):
    """Renames files in a folder by removing characters from the end of the filename."""
    path = Path(folder_path)
    for file in path.glob(f"*{file_type}"):
        if file.is_file():
            new_name = file.with_name(f"{file.stem[:slice_index]}{file.suffix}")
            file.rename(new_name)
            print(f"Renamed '{file.name}' to '{new_name.name}'")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python rename_script.py <folder_path> <file_type> <slice_index>", file=sys.stderr)
        sys.exit(1)
    
    try:
        rename_files(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)