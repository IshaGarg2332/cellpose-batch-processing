import os
import sys
import shutil
from pathlib import Path

def copy_all_c2_files(main_input, main_output):
    input_root = Path(main_input)
    output_root = Path(main_output)

    for folder in sorted(input_root.iterdir()):
        if not folder.is_dir():
            continue

        input_folder = folder
        output_folder = output_root / folder.name
        output_folder.mkdir(parents=True, exist_ok=True)

        for file in input_folder.iterdir():
            if file.is_file() and "c2" in file.name.lower():
                dest = output_folder / file.name
                if not dest.exists():
                    shutil.copy(file, dest)
                    print(f"✅ Copied: {file.name}")
                else:
                    print(f"⚠️ Skipped (already exists): {file.name}")

    print("\n🎉 Done copying all c2 files!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy_c2_simple.py <main_input_folder> <main_output_folder>")
    else:
        copy_all_c2_files(sys.argv[1], sys.argv[2])
