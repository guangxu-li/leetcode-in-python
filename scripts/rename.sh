#!/bin/bash

# Scan all files matching [0-9]+.<anything>.py and pad leading number to 4 digits
# Works recursively from the current directory (or pass a path as argument)

ROOT="${1:-.}"

find "$ROOT" -type f -name "*.py" | while read -r filepath; do
    dir=$(dirname "$filepath")
    filename=$(basename "$filepath")

    # Match files like: 1.foo.py, 23.bar.py, 123.baz.py, etc.
    if [[ "$filename" =~ ^([0-9]+)(\..+\.py)$ ]]; then
        num="${BASH_REMATCH[1]}"
        rest="${BASH_REMATCH[2]}"

        # Pad number to 4 digits
        padded=$(printf "%04d" "$num")
        new_filename="${padded}${rest}"

        if [[ "$filename" != "$new_filename" ]]; then
            echo "Renaming: $filepath -> $dir/$new_filename"
            mv -- "$filepath" "$dir/$new_filename"
        fi
    fi
done

echo "Done."
