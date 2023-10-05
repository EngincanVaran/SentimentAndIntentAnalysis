import argparse
import configparser
import logging
import os
from pathlib import Path

from utils import decide_on_verdict
from utils import load_model
from utils import load_transcript
from utils import write_results


def main(args, config):
    intents = config.get("classification", "intents")
    sentiments = config.get("classification", "sentiments")

    transcript_filename = args["transcript"]
    data = load_transcript(transcript_filename)
    model = load_model()

    logging.info("Preparing data... ")
    sentences = [step["content"] for step in data]

    logging.info("Making sentiment classifications...")
    sentiment_results = model(sentences, sentiments)
    sentiment_results = decide_on_verdict(sentiment_results)
    write_results(sentiment_results, transcript_filename, "sentiment")

    logging.info("Making intent classifications...")
    intent_results = model(sentences, intents)
    intent_results = decide_on_verdict(intent_results)
    write_results(intent_results, transcript_filename, "intent")

    logging.info("Finished with classifications...")

    logging.info("Done with everything...")


if __name__ == "__main__":
    # locate and read config.ini file
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "config", "config.ini")
    config = configparser.ConfigParser()
    config.read(config_path)

    # set up a basic logging mechanism
    logging.basicConfig(
        level=config.getint("logging", "LOG_LEVEL"),
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )

    # since we want to run this script with multiple inputs
    # we want to implement an argument parser
    parser = argparse.ArgumentParser(
        description="Sentiment and Intent Analysis Arguments Docstrings!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--transcript", "-t", default="transcript_0", type=str, help="The filename to analyze in json.")

    args = parser.parse_args()

    # call main
    main(vars(args), config)
