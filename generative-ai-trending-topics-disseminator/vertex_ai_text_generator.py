# vertex_ai_text_generator.py

import vertexai
from vertexai.language_models import TextGenerationModel
from gcp_helper import write_in_gsheet, sort_sheet
import re

def init_vertexai():
    vertexai.init(project="abhinav-dev", location="us-central1")
    return TextGenerationModel.from_pretrained("text-bison@001")

def predict(model, input_text):
    parameters = {
        "temperature": 0.2,
        "max_output_tokens": 1024,
        "top_p": 0.8,
        "top_k": 40
    }
    response = model.predict(input_text, **parameters)
    return response.text

def get_terms(topic_name):
    model = init_vertexai()
    input_text = f"list 100 trending topics in {topic_name}. Don\'t list their definitions. just the terms need to be listed"
    response_text = predict(model, input_text)
    print(response_text)
    glossary_list = re.findall(r"\d+\.\s+(.*)\n", response_text)
    print(glossary_list)
    return glossary_list

def ask_bard_explanation(random_term, topic_name):
    model = init_vertexai()
    input_text = f"Explain the trending topic {random_term} in {topic_name}. Also, include some relevant website links at the end for detailed explanation"
    explanation = predict(model, input_text)
    print(explanation)
    return explanation

def update_sheet_with_terms(INPUT_GSHEET_NAME, topic_name):
    for i in range(5):
        topics_list = get_terms(topic_name)
        write_in_gsheet(INPUT_GSHEET_NAME, topic_name, topics_list)
        sort_sheet(INPUT_GSHEET_NAME, topic_name)
