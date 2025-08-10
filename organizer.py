#!/usr/bin/env python3
import os
import shutil

# Define folders for file types
DIRECTORIES = {
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".tar", ".gz"],
    "Scripts": [".py", ".sh"],
}

# Path to organize (change this to your messy folder!)
target_dir = "/path/to/your/messy/folder"  # 🚨 Update this path!

def create_folders():
    """Create folders if they don't exist."""
    for folder in DIRECTORIES:
        if not os.path.exists(f"{target_dir}/{folder}"):
            os.mkdir(f"{target_dir}/{folder}")

def organize_files():
    """Move files to their respective folders."""
    for file in os.listdir(target_dir):
        file_path = os.path.join(target_dir, file)
        if os.path.isfile(file_path):
            for folder, extensions in DIRECTORIES.items():
                if any(file.endswith(ext) for ext in extensions):
                    shutil.move(file_path, f"{target_dir}/{folder}/{file}")
                    print(f"Moved: {file} → {folder}/")
                    break

if __name__ == "__main__":
    print("🚀 Starting file organization...")
    create_folders()
    organize_files()
    print("✅ Done!")
