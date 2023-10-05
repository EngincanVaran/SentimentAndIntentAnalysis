# Sentiment And Intent Analysis

## Overview

This project involves creating an English transcript of a conversation between a representative and a customer using ChatGPT. The conversation should consist of approximately 20 steps, with the customer expressing the intention to purchase an iPhone 14.

The primary goal of this project is to develop a codebase that utilizes a large language model to perform Sentiment Analysis (positive, negative, neutral) and Intention Prediction (e.g., 'change_package,' 'upgrade,' etc.) using Zero-Shot Learning.

## Project Structure

The project should have the following directory structure:

- `src`: This directory contains the source code for the system.
- `config`: Here, you can store model configurations, preferably in .ini format.
- `data`: This directory holds the simulated conversation data created with ChatGPT.
- `resources`: Store the pretrained zero-shot model here. You can use the Hugging Face zero-shot model, such as [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli).

## Getting Started

Follow these steps to set up and run the project:

1. Clone the repository:
   ```sh
   git clone https://github.com/EngincanVaran/SentimentAndIntentAnalysis.git

2. Navigate to the project directory:
   ```sh
    cd SentimentAndIntentAnalysis

3. Create a virtual environment and activate it (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate

4. Install the required dependencies:
   ```sh
   pip-compile requirements.in
   pip install -r requirements.txt

5. Run the code to perform Sentiment Analysis and Intention Prediction using the provided data and model:
   ```sh
   python main.py -t transcript_0
   - --transcript or -t: Provide the path to the JSON transcript file (required).

## Usage
To use the system, you can modify the main.py script to adapt it to your specific needs. This script should load the data, model, and configurations and perform Sentiment Analysis and Intention Prediction on the conversation.

## Pre-Commit
Getting Started
1. Before using pre-commit in your project, make sure you have it installed. You can install it globally or locally as a development dependency using pip:
   ```sh
   pip install pre-commit
   ```
2. Once you've configured pre-commit, you can run it before each commit by executing the following command:
   ```sh
   pre-commit run --all-files
   ```


## Acknowledgments
We would like to acknowledge the contributions of the open-source community and the Hugging Face Transformers library, which has been instrumental in developing this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
