# utils/data_handler.py

def resolve_conflicts_and_missing_values(normalized_data):
    """
    Resolves conflicts and handles missing values in normalized competitor data.
    If multiple entries for the same competitor (identified by 'name') exist, they are merged.

    Strategies:
    - Missing values:
      - For textual fields (e.g., 'description'), if missing or empty, set a default message.
      - For list fields (e.g., 'features'), ensure the value is a list.
    - Data conflicts:
      - If two entries for the same competitor have different descriptions, the function
        will combine them, unless one is a default placeholder.
      - For features, the function takes the union of both lists (removing duplicates).
      - It also tracks all sources that mentioned the competitor.
    
    :param normalized_data: List of dictionaries containing normalized competitor data.
    :return: List of merged competitor data entries.
    """
    merged_data = {}

    for entry in normalized_data:
        # Use the competitor name as the key. If the name is missing, skip the entry.
        name = entry.get("name", "").strip()
        if not name:
            continue

        # Handle missing values:
        description = entry.get("description", "").strip() or "No description available."
        features = entry.get("features", [])
        if not isinstance(features, list):
            features = []

        # If an entry with the same competitor name already exists, merge the data.
        if name in merged_data:
            existing = merged_data[name]

            # Merge description:
            # If one of the descriptions is just the default message, choose the non-default one.
            # Otherwise, combine both descriptions.
            if (existing["description"] == "No description available." and description != "No description available."):
                merged_description = description
            elif (description == "No description available." and existing["description"] != "No description available."):
                merged_description = existing["description"]
            elif description != existing["description"]:
                # Combine both descriptions to preserve all information.
                merged_description = existing["description"] + " " + description
            else:
                merged_description = existing["description"]

            # Merge features: take the union of both feature lists, removing duplicates.
            merged_features = list(set(existing["features"]) | set(features))

            # Merge source information:
            merged_sources = existing["sources"]
            source = entry.get("source", "Unknown")
            if source not in merged_sources:
                merged_sources.append(source)

            # Update the existing entry.
            merged_data[name]["description"] = merged_description
            merged_data[name]["features"] = merged_features
            merged_data[name]["sources"] = merged_sources
        else:
            # Create a new entry for this competitor.
            merged_data[name] = {
                "source": entry.get("source", "Unknown"),  # primary source
                "sources": [entry.get("source", "Unknown")],
                "name": name,
                "description": description,
                "features": features,
            }

    # Return the merged data as a list of competitor entries.
    return list(merged_data.values())


if __name__ == "__main__":
    # Example usage of the data handler function
    sample_data = [
        {"source": "Crunchbase", "name": "StartupX", "description": "Innovative tech startup.", "features": ["AI", "Cloud"]},
        {"source": "LinkedIn", "name": "StartupX", "description": "", "features": ["Cloud", "Mobile"]},
        {"source": "Reddit", "name": "StartupY", "description": None, "features": ["E-commerce"]},
        {"source": "Google", "name": "StartupZ", "description": "Emerging player in fintech.", "features": "Not a list"},
    ]

    # Normalize sample_data by ensuring that all fields are in the correct format,
    # then resolve conflicts and missing values.
    resolved = resolve_conflicts_and_missing_values(sample_data)
    for competitor in resolved:
        print(competitor)
