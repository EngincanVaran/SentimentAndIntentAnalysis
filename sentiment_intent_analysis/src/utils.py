import json
import logging

from transformers import pipeline


def load_transcript(transcript_filename):
    TRANSCRIPT_PATH = f"../data/input/{transcript_filename}.json"
    logging.info(f"Loading transcript... {transcript_filename}")
    with open(TRANSCRIPT_PATH) as f:
        data = json.load(f)
        return data


def load_model():
    model_name = "facebook/bart-large-mnli"
    logging.info(f"Loading Model... {model_name}")
    classifier = pipeline("zero-shot-classification", model=model_name)
    return classifier


def write_results(result, transcript_filename, classification_type):
    TRANSCRIPT_PATH = f"../data/output/{transcript_filename}_{classification_type}_result.json"
    logging.info(f"Writing result... {transcript_filename}_{classification_type}")
    with open(TRANSCRIPT_PATH, "w") as f:
        json.dump(result, f, indent=4)


def decide_on_verdict(result):
    for step in result:
        step["verdict"] = [step["labels"][0], step["scores"][0]]
    return result
