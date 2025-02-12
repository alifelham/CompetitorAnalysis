# agents/feature_comparison_agent.py
class FeatureComparisonAgent:
    def compare(self, normalized_data):
        """
        Compare features across competitors.
        Returns a summary of common features and feature occurrence.
        """
        feature_map = {}
        for entry in normalized_data:
            features = entry.get("features", [])
            for feature in features:
                feature_map[feature] = feature_map.get(feature, 0) + 1
        common_features = [feature for feature, count in feature_map.items() if count > 1]
        return {"common_features": common_features, "all_features": feature_map}
