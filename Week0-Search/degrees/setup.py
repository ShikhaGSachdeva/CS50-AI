"""
Setup script for CS50 AI — Week 0: Degrees of Separation
Downloads and extracts the required IMDb dataset automatically.
Works on Mac, Windows, and Linux.
"""

import urllib.request
import zipfile
import os
import sys
import shutil

DATASET_URL = "https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip"
ZIP_FILE = "degrees.zip"
REQUIRED_FOLDERS = ["large", "small"]
REQUIRED_FILES = [
    "large/people.csv",
    "large/movies.csv",
    "large/stars.csv",
    "small/people.csv",
    "small/movies.csv",
    "small/stars.csv",
]


def dataset_exists():
    """Check if dataset is already fully present."""
    return all(os.path.exists(f) for f in REQUIRED_FILES)


def download_dataset():
    """Download the degrees dataset from CS50."""

    if dataset_exists():
        print("✅ Dataset already exists — nothing to download.")
        return

    print("📥 Downloading dataset from CS50...")
    print(f"   Source: {DATASET_URL}")

    try:
        def progress(count, block_size, total_size):
            if total_size > 0:
                percent = min(int(count * block_size * 100 / total_size), 100)
                sys.stdout.write(f"\r   Progress: {percent}%")
                sys.stdout.flush()

        urllib.request.urlretrieve(DATASET_URL, ZIP_FILE, reporthook=progress)
        print("\n✅ Download complete.")

    except Exception as e:
        print(f"\n❌ Download failed: {e}")
        print("   Please download manually from:")
        print(f"   {DATASET_URL}")
        sys.exit(1)


def extract_dataset():
    """Extract the downloaded zip file, handling nested folder structure."""

    if dataset_exists():
        return

    print("📦 Extracting dataset...")

    # Extract everything into a temp folder to avoid conflicts
    temp_dir = "_temp_extract"

    try:
        # Clean up any previous temp extraction
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

        os.makedirs(temp_dir)

        # Extract all contents into temp folder
        with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        # Find where large/ and small/ actually ended up
        # They may be at root or inside a subfolder like degrees/
        source_root = temp_dir
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            if os.path.isdir(item_path):
                # Check if large/ and small/ are inside this subfolder
                if os.path.exists(os.path.join(item_path, "large")) or \
                   os.path.exists(os.path.join(item_path, "small")):
                    source_root = item_path
                    break

        # Copy large/ and small/ to current directory
        for folder in REQUIRED_FOLDERS:
            src = os.path.join(source_root, folder)
            dst = folder

            if not os.path.exists(src):
                continue

            # Remove existing destination if present
            if os.path.exists(dst):
                shutil.rmtree(dst)

            shutil.copytree(src, dst)
            print(f"   ✅ Extracted {folder}/")

        print("✅ Extraction complete.")

    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        sys.exit(1)

    finally:
        # Always clean up temp folder
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)


def cleanup():
    """Remove the zip file after extraction."""
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)
        print("🧹 Cleaned up zip file.")


def verify():
    """Verify the dataset was extracted correctly."""
    missing = [f for f in REQUIRED_FILES if not os.path.exists(f)]

    if not missing:
        print("✅ Dataset verified — all required files present.")
        print("\n🚀 Ready to run:")
        print("   python degrees.py small")
        print("   python degrees.py large")
    else:
        print("❌ Some files are missing:")
        for f in missing:
            print(f"   - {f}")
        sys.exit(1)


if __name__ == "__main__":
    print("=" * 50)
    print("  CS50 AI — Degrees Dataset Setup")
    print("=" * 50)
    download_dataset()
    extract_dataset()
    cleanup()
    verify()
    print("=" * 50)
