# agents/nlp_processing_agent.py

import spacy
from textblob import TextBlob

class NLPProcessingAgent:
    def __init__(self):
        # Load the small English model for spaCy.
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, normalized_data):
        """
        Process normalized competitor data to extract key NLP insights.
        
        For each entry, the following are added:
          - summary: The first sentence of the description.
          - named_entities: A list of tuples containing entity text and label.
          - sentiment: A dictionary with polarity and subjectivity.
          - token_count: The number of tokens in the description.
        
        :param normalized_data: List of dictionaries with competitor data.
        :return: List of dictionaries with added NLP insights.
        """
        processed = []
        for entry in normalized_data:
            description = entry.get("description", "").strip()
            
            if description:
                # Process the description using spaCy
                doc = self.nlp(description)
                
                # Extract summary: the first sentence of the document.
                sentences = list(doc.sents)
                summary = sentences[0].text if sentences else description
                
                # Extract named entities
                named_entities = [(ent.text, ent.label_) for ent in doc.ents]
                
                # Compute sentiment using TextBlob
                blob = TextBlob(description)
                sentiment = {
                    "polarity": blob.sentiment.polarity,
                    "subjectivity": blob.sentiment.subjectivity
                }
                
                # Count tokens in the description
                token_count = len(doc)
            else:
                summary = ""
                named_entities = []
                sentiment = {"polarity": 0.0, "subjectivity": 0.0}
                token_count = 0

            # Add the new NLP insights to the entry
            entry["summary"] = summary
            entry["named_entities"] = named_entities
            entry["sentiment"] = sentiment
            entry["token_count"] = token_count

            processed.append(entry)
        return processed
