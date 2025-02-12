# agents/report_generation_agent.py
def build_competitor_profile(entry):
    return (
        f"Name: {entry.get('name')}\n"
        f"Description: {entry.get('description')}\n"
        f"Summary: {entry.get('summary')}\n"
        f"Features: {', '.join(entry.get('features', []))}\n"
    )

class ReportGenerationAgent:
    def generate_report(self, normalized_data, swot_analysis):
        report = "# Competitor Analysis Report\n\n"
        for entry, analysis in zip(normalized_data, swot_analysis):
            profile = build_competitor_profile(entry)
            report += f"### {entry.get('name')}\n\n"
            report += f"{profile}\n"
            report += f"**SWOT Analysis:**\n{analysis.get('swot', 'No SWOT analysis available.')}\n\n"
            report += "---\n\n"
        return report
