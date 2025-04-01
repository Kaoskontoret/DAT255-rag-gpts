# GPT Models Experimentation with RAG Techniques

[![CI Workflow](https://github.com/your-username/your-repo/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/your-username/your-repo/actions/workflows/CI.yml)
[![Build and Push Image](https://github.com/your-username/your-repo/actions/workflows/build-and-push-image-to-ghcr.yml/badge.svg?branch=main)](https://github.com/your-username/your-repo/actions/workflows/build-and-push-image-to-ghcr.yml)
[![Ruff format](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FJacobCoffee%2Fbfb02a83c8da3cbf53f7772f2cee02ec%2Fraw%2Facb94daa3aedecda67e2c7d8c5aec9765db0734d%2Fformat-badge.json)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Hi there! :wave:  
This repository is dedicated to exploring and experimenting with GPT-based models—both pretrained and self-trained—with a focus on integrating Retrieval-Augmented Generation (RAG) techniques. The goal of the project is to investigate whether we can train our own GPT model and make it work effectively with RAG methods.

## Project Overview

This project is organized into several modules:
- **Pretrained Models:** Modules for working with popular pretrained models (e.g., GPT-2 from Hugging Face).
- **Self-Trained Models:** Code to train or fine-tune your own GPT model.
- **RAG Techniques:** Integration of retrieval mechanisms to enhance the generation quality of GPT models.

## Features

- **Modular Codebase:**  
  Separate modules for pretrained and self-trained GPT models, as well as RAG integration, to facilitate experimentation and development.

- **Console Application:**  
  An interactive console app that demonstrates how to load a GPT model, prompt the user for input, and generate text.

- **Local Model Storage:**  
  Easily save and load GPT models from a local directory to avoid unnecessary downloads and to support offline work.

- **Configuration Management:**  
  Utilize configuration files to manage environment variables and secrets, ensuring sensitive data is kept secure across different environments.

- **CI/CD and Code Quality:**  
  Preconfigured workflows for continuous integration and automated builds are available. Code formatting and linting are enforced using tools like Ruff.

## Getting Started

### Prerequisites

- **Python:** Version 3.8 or later  
- **PyTorch:** Ensure compatibility with your hardware (GPU support if available)  
- **Transformers:** Hugging Face Transformers library for model management

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies with `pyproject.toml`:**

   ```bash
   pip install -e .
   ```

   Make sure you have a valid `pyproject.toml` file with the required dependencies listed under `[project]` or `[tool.poetry.dependencies]`.

### ML-Models are not included. And should be downloaded and added to this folder:

```bash
./ml-modles/nameofmodel/
```

### Running the Console Application

Run the following command from the project root:

```bash
python app.py
```

Follow the on-screen instructions to interact with the GPT model via the console.




## Configuration and Secrets

- **Configuration Files:**  
  The project includes configuration files for local, development, and production environments. These files help manage sensitive environment variables securely.

- **GitHub Secrets:**  
  When deploying or running tests on GitHub, ensure that your secrets are set up to match the variable names in the configuration files (e.g., `ENV_MODEL_URL`).

## Project Goals

- **Custom GPT Model Training:**  
  Experiment with training our own GPT model or fine-tuning a pretrained model to suit your specific needs.

- **RAG Integration:**  
  Explore techniques to combine retrieval methods with generative models, aiming to enhance text generation quality and relevance.

- **Reproducibility:**  
  By pinning dependency versions and using configuration files, the project aims for reproducible and manageable experiments.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.


Happy coding and experimenting with GPT models and RAG techniques!

