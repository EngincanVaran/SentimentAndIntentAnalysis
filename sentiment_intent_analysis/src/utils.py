import json
import logging
import os
from pathlib import Path
from typing import Dict
from typing import List

from transformers import Pipeline
from transformers import pipeline


def load_transcript(transcript_filename) -> list[dict]:
    TRANSCRIPT_PATH = f"../data/input/{transcript_filename}.json"
    logging.info(f"Loading transcript... {transcript_filename}")
    with open(TRANSCRIPT_PATH) as f:
        data = json.load(f)
        return data


def load_model() -> Pipeline:
    model_name = "bart-large-mnli"
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.absolute()
    model_path = os.path.join(ROOT_DIR, "resources", model_name)
    # check if we are already downloaded the model
    # if so load it, else download from huggingface
    if os.path.exists(model_path) and os.path.isdir(model_path):
        logging.info("Found the model in locally, Loading the model...")
        classifier = pipeline("zero-shot-classification", model_path)
    else:
        model_name = "facebook/bart-large-mnli"
        logging.info(f"Loading Model... {model_name}")
        classifier = pipeline("zero-shot-classification", model_name)
        classifier.save_pretrained(model_path)
    return classifier


def write_results(result, transcript_filename, classification_type) -> None:
    TRANSCRIPT_PATH = f"../data/output/{transcript_filename}_{classification_type}_result.json"
    logging.info(f"Writing result... {transcript_filename}_{classification_type}")
    with open(TRANSCRIPT_PATH, "w") as f:
        json.dump(result, f, indent=4)


def decide_on_verdict(result) -> list[dict]:
    for step in result:
        step["verdict"] = [step["labels"][0], step["scores"][0]]
    return result
