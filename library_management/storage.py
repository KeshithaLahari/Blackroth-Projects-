"""Simple JSON file storage for books, members, and issues."""

import json
import os


class JSONStorage:
    """Read and write list data to JSON files."""

    def load(self, filepath: str) -> list[dict]:
        """Load data from a JSON file. Return empty list if file doesn't exist."""
        if not os.path.exists(filepath):
            return []

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception:
            return []

    def save(self, filepath: str, data: list[dict]) -> None:
        """Save a list of dictionaries into a clean JSON file."""
        # Ensure the directory exists
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)