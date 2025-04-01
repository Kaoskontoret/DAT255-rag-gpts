import os
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT2Console:
    def __init__(self, model_path="../../ml-model/gpt2/"):
        """
        Initialize GPT2Console by loading the tokenizer and model from the local directory.
        Adjust the relative path if necessary based on your project structure.
        """
        # Convert the model path to an absolute path
        abs_model_path = os.path.abspath(model_path)
        print(f"Loading model from: {abs_model_path}")
        
        # Load the tokenizer and model from the local directory using local_files_only
        self.tokenizer = GPT2Tokenizer.from_pretrained(abs_model_path, local_files_only=True)
        self.model = GPT2LMHeadModel.from_pretrained(abs_model_path, local_files_only=True)
        self.model.eval()

    def generate_text(self, prompt, max_length=100):
        """
        Generate text based on the given prompt.

        Args:
            prompt (str): The input text prompt.
            max_length (int): The maximum length of the generated sequence.

        Returns:
            str: The generated text.
        """
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                early_stopping=True
            )
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
