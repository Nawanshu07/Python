"""
remove_duplicate_songs.py
--------------------------
Scans a folder for duplicate audio files using TWO methods:
  1. Name-based: same base name with - Copy / (1) / (2) suffixes
  2. Hash-based: files with identical content (even if names differ)

Keeps ONE copy per duplicate group (largest file, or alphabetically first on tie).

Supported formats: .mp3 .flac .wav .aac .ogg .m4a .wma .opus .aiff .ape

Usage:
    python remove_duplicate_songs.py <folder_path> [--dry-run]

Options:
    --dry-run   Show what would be deleted without actually deleting anything.
"""

import os
import sys
import re
import hashlib
from collections import defaultdict

AUDIO_EXTENSIONS = {".mp3", ".flac", ".wav", ".aac", ".ogg", ".m4a", ".wma", ".opus", ".aiff", ".ape"}


def file_hash(path: str) -> str:
    """Return MD5 hash of file contents."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()


def strip_copy_suffixes(name: str) -> str:
    """Remove duplicate suffixes: '- Copy', '(1)', '(2)', etc."""
    name = re.sub(r'\s*-\s*copy(\s*\(\d+\))?$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(\d+\)$', '', name)
    return name.strip().lower()


def choose_keeper(paths: list) -> str:
    """Keep the largest file; tie-break: shortest (cleanest) filename."""
    return max(paths, key=lambda p: (os.path.getsize(p), -len(os.path.basename(p))))


def find_duplicates(folder: str):
    """
    Returns list of groups, each group is a list of paths that are duplicates.
    Uses both name-matching AND hash-matching.
    """
    all_audio = []
    for entry in os.scandir(folder):
        if entry.is_file():
            _, ext = os.path.splitext(entry.name)
            if ext.lower() in AUDIO_EXTENSIONS:
                all_audio.append(entry.path)

    # --- Pass 1: Group by canonical name (handles - Copy, (1), (2) etc.) ---
    name_groups = defaultdict(list)
    for path in all_audio:
        base, _ = os.path.splitext(os.path.basename(path))
        canonical = strip_copy_suffixes(base)
        name_groups[canonical].append(path)

    # Flatten: collect files already identified as duplicates by name
    name_duplicates = {name: paths for name, paths in name_groups.items() if len(paths) > 1}

    # --- Pass 2: Hash remaining files to catch identical-content duplicates ---
    # Files already handled by name grouping can also be double-checked via hash
    hash_groups = defaultdict(list)
    for path in all_audio:
        h = file_hash(path)
        hash_groups[h].append(path)

    hash_duplicates = {h: paths for h, paths in hash_groups.items() if len(paths) > 1}

    # --- Merge both sets of duplicates ---
    # Use path sets to avoid double-counting
    seen_groups = []
    processed_paths = set()

    for name, paths in name_duplicates.items():
        group = sorted(set(paths))
        key = frozenset(group)
        if key not in [frozenset(g) for g in seen_groups]:
            seen_groups.append(group)
            processed_paths.update(group)

    for h, paths in hash_duplicates.items():
        group = sorted(set(paths))
        key = frozenset(group)
        if key not in [frozenset(g) for g in seen_groups]:
            seen_groups.append(group)
            processed_paths.update(group)

    return seen_groups


def remove_duplicates(folder: str, dry_run: bool = False):
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Scanning: {folder}")
    print("(This may take a moment while hashing files...)\n")

    groups = find_duplicates(folder)

    if not groups:
        print("✅ No duplicates found.")
        return

    total_deleted = 0
    total_freed = 0

    for paths in sorted(groups, key=lambda g: os.path.basename(g[0]).lower()):
        keeper = choose_keeper(paths)
        to_delete = [p for p in paths if p != keeper]

        print(f"🎵 '{os.path.basename(keeper)}'  ({len(paths)} copies)")
        print(f"   ✔  KEEP   : {os.path.basename(keeper)}  ({os.path.getsize(keeper):,} bytes)")

        for path in to_delete:
            size = os.path.getsize(path)
            print(f"   ✖  DELETE : {os.path.basename(path)}  ({size:,} bytes)")
            if not dry_run:
                os.remove(path)
            total_deleted += 1
            total_freed += size

        print()

    action = "Would free" if dry_run else "Freed"
    verb = "would be " if dry_run else ""
    print(f"{'[DRY RUN] ' if dry_run else ''}Done. {total_deleted} file(s) {verb}deleted. {action} {total_freed / (1024*1024):.2f} MB.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python remove_duplicate_songs.py <folder_path> [--dry-run]")
        sys.exit(1)

    folder_path = sys.argv[1]
    dry_run_mode = "--dry-run" in sys.argv

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a valid directory.")
        sys.exit(1)

    remove_duplicates(folder_path, dry_run=dry_run_mode)