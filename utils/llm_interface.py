import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_swot_analysis(profile):
    prompt = (
        "Below is a competitor profile. Based on the details provided, produce a detailed SWOT analysis "
        "with the following sections:\n"
        "1. Strengths\n"
        "2. Weaknesses\n"
        "3. Opportunities\n"
        "4. Threats\n\n"
        "Competitor Profile:\n"
        f"{profile}\n\n"
        "Please provide the SWOT analysis in a clear and organized manner. Do not ask any clarifying questions; "
        "simply generate the analysis based on the information given."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Adjust the model as needed
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a competitor analysis expert. When provided with a competitor profile, "
                        "you produce a detailed SWOT analysis with the sections: Strengths, Weaknesses, Opportunities, and Threats. "
                        "Do not ask for additional information; simply analyze the given profile."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=250,
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error generating SWOT analysis: {e}")
        return "SWOT analysis could not be generated."
