"""Module docstring. Write something clever."""

import logging
import logging.config
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from config.config import get_config
from examplepackage.example_module import Aclass


_CONFIG = get_config()
_LOGGER = logging.getLogger(__name__)
if _CONFIG.logging is not None:
    logging.config.dictConfig(_CONFIG.logging)
_LOGGER.debug("Some configs..")
_LOGGER.debug(_CONFIG)
_LOGGER.debug("Starting soonish")

from transformerspackage.gptmodel import GPT2Console

def main():
    # Instantiate the GPT2Console class.
    # Adjust the model_path if your working directory differs from project root.
    gpt_console = GPT2Console(model_path="./ml-models/gpt2/")
    
    print("Welcome to the GPT-2 Console Program!")
    print("Type your prompt and press enter. Type 'exit' to quit.")
    
    while True:
        prompt = input("\nEnter prompt: ")
        if prompt.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        generated = gpt_console.generate_text(prompt, max_length=150)
        print("\nGenerated text:\n", generated)

if __name__ == "__main__":
    _LOGGER.debug("Starting")
    main()
    _LOGGER.info("Ending")
    _LOGGER.debug("")
    _LOGGER.warning("")
    _LOGGER.error("")
    _LOGGER.critical("")
