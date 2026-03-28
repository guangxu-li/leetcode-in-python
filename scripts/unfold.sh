#!/bin/bash

# Unfold all [0-9]+.*\.py files from subdirectories into the current directory
# Usage: bash unfold.sh [source_root]
# If source_root is omitted, searches subdirectories of current directory

SOURCE="${1:-.}"
DEST="$(pwd)"

find "$SOURCE" -mindepth 2 -type f -name "*.py" | while read -r filepath; do
    filename=$(basename "$filepath")

    # Only process files matching [0-9]+.<anything>.py
    if [[ "$filename" =~ ^[0-9]+\..+\.py$ ]]; then
        dest_file="$DEST/$filename"

        # Handle filename collisions
        if [[ -e "$dest_file" ]]; then
            echo "SKIP (exists): $filename"
        else
            echo "Moving: $filepath -> $dest_file"
            mv -- "$filepath" "$dest_file"
        fi
    fi
done

# Remove empty directories left behind (excluding the source root itself)
find "$SOURCE" -mindepth 1 -type d -empty -delete 2>/dev/null

echo "Done."
