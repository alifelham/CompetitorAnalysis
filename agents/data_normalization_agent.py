# agents/data_normalization_agent.py
from utils.data_handler import resolve_conflicts_and_missing_values

class DataNormalizationAgent:
    def normalize(self, raw_data):
        """
        Normalize raw data from various sources into a consistent structure.
        Adjust the fields for sources that use non-standard keys.
        """
        normalized = []
        for source, data in raw_data.items():
            if data is None:
                continue

            # For Google, extract the company name and description from "title" and "snippet"
            if source == "Google":
                name = data.get("title", "").strip()
                description = data.get("snippet", "").strip()
                features = []  # Google results usually don't include structured features.
            else:
                name = data.get("name", "").strip()
                description = data.get("description", "").strip()
                features = data.get("features", [])
                if not isinstance(features, list):
                    features = []

            entry = {
                "source": source,
                "name": name,
                "description": description,
                "features": features,
            }
            normalized.append(entry)

        # Merge data from multiple sources, fill in missing values, and resolve conflicts.
        normalized = resolve_conflicts_and_missing_values(normalized)
        return normalized
