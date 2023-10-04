import json
import logging


def load_transcript(transcript_filename):
    TRANSCRIPT_PATH = f"../data/{transcript_filename}.json"
    logging.info(f"Using transcript: {transcript_filename}")
    with open(TRANSCRIPT_PATH) as f:
        data = json.load(f)
        return data
