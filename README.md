# Multi-Agent Competitor Analysis System

## Overview

The **Multi-Agent Competitor Analysis System** is an automated platform that generates comprehensive SWOT analyses for companies using minimal user input. Simply by providing a company name (e.g., "Adobe"), the system:
- Aggregates data from multiple trusted sources (Crunchbase, LinkedIn, Google Custom Search, G2).
- Normalizes and enriches the collected data using NLP techniques (spaCy, TextBlob).
- Leverages a state-of-the-art Large Language Model (LLM) via the OpenAI API to produce a detailed SWOT analysis.
- Compiles the information into a final report.

This project uses a modular, multi-agent architecture that separates data retrieval, normalization, enrichment, SWOT analysis generation, and report creation into distinct components.

---

## Features

- **Multi-Agent Architecture:** Modular design for improved scalability and maintainability.
- **Automated Data Collection:** Fetches company data from multiple APIs (Crunchbase, LinkedIn, Google Custom Search, G2).
- **Data Normalization & Enrichment:** Standardizes data from diverse sources and enriches it using NLP (spaCy, TextBlob).
- **SWOT Analysis Generation:** Uses the OpenAI Chat Completion API (GPT-4 or GPT-3.5 Turbo) to generate detailed SWOT analyses.
- **Comprehensive Reporting:** Produces a final Markdown report that can be converted to PDF.

---

## Architectural Diagram

Below is a Mermaid diagram that illustrates the system’s architecture:

```
mermaid
flowchart TD
    A[Orchestrator (main.py)]
    B[Data Retrieval Agent]
    C[Data Normalization Agent]
    D[NLP Processing Agent]
    E[SWOT Analysis Agent]
    F[Report Generation Agent]

    A --> B
    A --> C
    A --> D
    B --> C
    C --> D
    D --> E
    E --> F
```
To generate an image or PDF of this diagram, paste the code into the Mermaid Live Editor and export the result.

```
competitor-analysis/
├── README.md
├── requirements.txt
├── main.py
├── agents/
│   ├── __init__.py
│   ├── data_retrieval_agent.py
│   ├── data_normalization_agent.py
│   ├── nlp_processing_agent.py
│   ├── swot_analysis_agent.py
│   └── report_generation_agent.py
├── utils/
│   ├── __init__.py
│   ├── data_handler.py
│   └── llm_interface.py
└── docs/
    └── Solution_Design_Document.pdf  # PDF version of the design document.
```

# Setup Instructions
## Prerequisites
- Python 3.8+
- Pip package manager

You will need valid API keys for:

- CRUNCHBASE_API_KEY
- LINKEDIN_ACCESS_TOKEN
- GOOGLE_API_KEY
- GOOGLE_CX
- G2_API_KEY
- OPENAI_API_KEY

# Installation (Using a Virtual Environment)

## Create and Activate a Virtual Environment:
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

## Install Dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```
# Set Up Environment Variables:
Create a .env file in the root directory with the following (replace placeholders with your actual keys):
```
CRUNCHBASE_API_KEY=your_crunchbase_api_key
LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CX=your_google_cx
G2_API_KEY=your_g2_api_key
OPENAI_API_KEY=your_openai_api_key
Make sure to add .env to your .gitignore to prevent accidental commits of your sensitive keys.
```
## Download the spaCy English Model:
```
python -m spacy download en_core_web_sm
```
## Running the Project
With the environment set up, run the project using:
```
python main.py
```
When prompted, enter a company name (e.g., "Adobe"). The system will:

- Retrieve data from Crunchbase, LinkedIn, Google Custom Search, and G2.
- Normalize and enrich the data.
- Generate a detailed SWOT analysis via the OpenAI API.
- Compile the results into a final report (competitor_analysis_report.md).

# Data Handling Strategies
For more details on how data is handled, refer to the Solution Design Document in the docs/ folder. Key points include:

- ETL Process: Extract, transform, and load data from multiple sources.
- Conflict Resolution: Merge overlapping data and fill in missing values using a dedicated utility.
- Data Enrichment: Use NLP techniques (spaCy, TextBlob) to extract summaries, named entities, and sentiment, ensuring a comprehensive company profile.
