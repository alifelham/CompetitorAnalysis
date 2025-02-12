# main.py
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from the .env file

from agents.data_retrieval_agent import DataRetrievalAgent
from agents.data_normalization_agent import DataNormalizationAgent
from agents.nlp_processing_agent import NLPProcessingAgent
from agents.swot_analysis_agent import SWOTAnalysisAgent
from agents.report_generation_agent import ReportGenerationAgent

def main(query):
    # Define the list of data sources. (Reddit has been removed.)
    sources = [
        {"name": "Crunchbase"},
        {"name": "LinkedIn"},
        {"name": "Google"},  # Google Custom Search will now be used instead of Reddit.
        {"name": "G2"}
    ]
    data_agent = DataRetrievalAgent(sources)
    raw_data = data_agent.fetch_data(query)
    
    normalization_agent = DataNormalizationAgent()
    normalized_data = normalization_agent.normalize(raw_data)
    
    nlp_agent = NLPProcessingAgent()
    processed_data = nlp_agent.process(normalized_data)
    
    swot_agent = SWOTAnalysisAgent()
    swot_results = swot_agent.analyze(processed_data)
    
    report_agent = ReportGenerationAgent()
    report = report_agent.generate_report(normalized_data, swot_results)
    
    with open("competitor_analysis_report.md", "w", encoding="utf-8") as file:
        file.write(report)
    print("Report generated successfully! Check 'competitor_analysis_report.md'.")

if __name__ == "__main__":
    input_query = input("Enter a company name: ")
    main(input_query)
