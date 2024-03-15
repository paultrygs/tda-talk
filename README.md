# Topology meets ML

The Jupyter notebook presentation.ipynb in this repository was used to deliver a talk on topological data analysis at an internal conference for Bouvet Norge. It contains code and images that illustrate an unsupervised method known as persistent homology. The content is designed for a general tech audience and does not require any advanced math knowledge.

## Setup on UNIX
Navigate to the root of the repository and run the following commands (bash):

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install poetry
poetry install
```

Now you are ready to run the notebook by typing:

```bash
jupyter lab
```

