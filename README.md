# CustomBERT model for learning, and experemetning about deep learning and NLP
## Template from setup is forked from frdedynamics, it is originally a basic template repo with devcontainers and workflows++
## IMOPORTANT This repository contains a lot of code that have been used to experiment with different problem statements. The important notebook however is [Encoder Only Notebook](https://github.com/Kaoskontoret/DAT255-rag-gpts/blob/main/src/transformerspackage/encoder_only_embedder_nn.ipynb). This contains all code relevant for the assignment

## The notebook have changed drastically over the training of the different models. And the models are localy downloaded on our computers. 
## It is developed and inspired by the known BERT architecture. We did not invent this, but have experimented with training it and building it using the torch framework

## To run the model the following steps are required. 
Download the requirements.txt

Clone the project to your own machine.
Create a viritual environment for example with
```python
python -m venv venv

```

Install requirements
```python
pip install -r requirements.txt
```

To run models, one only needs download the datasets using the relevant cells, and train the tokenizer. Some models have 30000 and some 10000 as vocab. This need to be alternated when running the different models. After the traing of custombert there are some cells for testing an loading models, and running tests. one Subjective top 10 predictions for us humans to enjoy, and a mlm evaluation cell under to use for metrics.

Some cells are developed passed what we have actually been able to train on, because the iterations took to much time. See it as a cookingstation where not all the pots have been properly cleaned...
