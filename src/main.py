import argparse
import configparser
import logging
import os
from pathlib import Path

from src.utils import load_transcript


def main(args, config):
    data = load_transcript(args["transcript"])


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
        handlers=[
            logging.StreamHandler()
        ]
    )

    # since we want to run this script with multiple inputs
    # we want to implement an argument parser
    parser = argparse.ArgumentParser(
        description="Sentiment and Intent Analysis Arguments Docstrings!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--transcript', '-t', default='transcript_0', type=str, help="The filename to analyze in json.")

    args = parser.parse_args()

    # call main
    main(args, config)