"""
Setup script for CS50 AI — Week 0: Degrees of Separation
Downloads and extracts the required IMDb dataset automatically.
"""

import urllib.request
import zipfile
import os
import sys

DATASET_URL = "https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip"
ZIP_FILE = "degrees.zip"


def download_dataset():
    """Download the degrees dataset from CS50."""

    # Check if dataset already exists
    if os.path.exists("large") and os.path.exists("small"):
        print("✅ Dataset already exists — nothing to download.")
        return

    print("📥 Downloading dataset from CS50...")
    print(f"   Source: {DATASET_URL}")

    try:
        # Show download progress
        def progress(count, block_size, total_size):
            percent = int(count * block_size * 100 / total_size)
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
    """Extract the downloaded zip file."""

    print("📦 Extracting dataset...")

    try:
        with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
            # Extract only large/ and small/ folders
            for member in zip_ref.namelist():
                # Strip the top-level degrees/ folder if present
                parts = member.split("/")
                if len(parts) > 1 and parts[0] == "degrees":
                    target = "/".join(parts[1:])
                    if target:
                        zip_ref.extract(member)
                        os.makedirs(os.path.dirname(target), exist_ok=True)
                        os.rename(member, target)
                else:
                    zip_ref.extract(member)

        print("✅ Extraction complete.")

    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        sys.exit(1)


def cleanup():
    """Remove the zip file after extraction."""
    if os.path.exists(ZIP_FILE):
        os.remove(ZIP_FILE)
        print("🧹 Cleaned up zip file.")

    # Clean up any empty degrees/ folder left behind
    if os.path.exists("degrees") and os.path.isdir("degrees"):
        try:
            os.rmdir("degrees")
        except OSError:
            pass


def verify():
    """Verify the dataset was extracted correctly."""
    required = [
        "large/people.csv",
        "large/movies.csv",
        "large/stars.csv",
        "small/people.csv",
        "small/movies.csv",
        "small/stars.csv",
    ]

    all_present = all(os.path.exists(f) for f in required)

    if all_present:
        print("✅ Dataset verified — all required files present.")
        print("\n🚀 Ready to run:")
        print("   python degrees.py small")
        print("   python degrees.py large")
    else:
        missing = [f for f in required if not os.path.exists(f)]
        print("❌ Some files are missing:")
        for f in missing:
            print(f"   - {f}")


if __name__ == "__main__":
    print("=" * 50)
    print("  CS50 AI — Degrees Dataset Setup")
    print("=" * 50)
    download_dataset()
    extract_dataset()
    cleanup()
    verify()
    print("=" * 50)
