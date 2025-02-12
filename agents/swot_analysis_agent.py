from utils.llm_interface import generate_swot_analysis

class SWOTAnalysisAgent:
    def analyze(self, processed_data):
        enriched_results = []
        for entry in processed_data:
            # Aggregate the detailed profile from the processed data.
            profile = (
                f"Name: {entry.get('name')}\n"
                f"Description: {entry.get('description')}\n"
                f"Summary: {entry.get('summary')}\n"
                f"Features: {', '.join(entry.get('features', []))}\n"
                f"Named Entities: {entry.get('named_entities', [])}\n"
                f"Sentiment: {entry.get('sentiment', {})}\n"
            )
            swot = generate_swot_analysis(profile)
            enriched_results.append({"swot": swot})
        return enriched_results
