# MTG Basic Lands Classifier

A Magic: The Gathering basic lands artwork classifier.

The model receives an artwork as input and predicts whether it's a Plains, Island, Swamp, Mountain or Forest.

![alt text](https://github.com/jansaldo/MTG-Basic-Lands-Classifier/blob/main/sample_preds.gif?raw=true "Sample predictions")
 
This repository contains the code that was used to develop the convolutional neural network using [TensorFlow](https://www.tensorflow.org/), as well as the source code of a [Streamlit](https://streamlit.io/) web app that let's you see the model in action. Data was collected using the [Scryfall API](https://scryfall.com/docs/api).


## Getting started

Clone this repository and navigate to it's folder.

```bash
git clone https://github.com/jansaldo/MTG-Basic-Lands-Classifier.git
cd MTG-Basic-Lands-Classifier
```

It's recommended to create a new virtual environment before installing the necessary packages.

If working with `conda`, run the following:

```bash
conda env create -f environment.yml
conda activate mtg_basics_clf
```

Alternatively, if working with `venv`, run:

```bash
sudo apt install python3-venv
python3 -m venv mtg_basics_clf
source mtg_basics_clf/bin/activate
pip install -r requirements.txt
```


## Machine learning workflow

The machine learning workflow, from data collection to model training and evaluation, can be followed with these notebooks:

- `notebooks/00_fetch_data.ipynb`: consumption of [Scryfall API](https://scryfall.com/docs/api) in order to fetch the available images of basic lands which are used to develop the classification model.
> Image files weren't uploaded to GitHub to keep the repository size small. To get the same dataset that was used to train and validate the model, navigate to the scripts directory from a terminal and run `get_imgs.py` instead of running this notebook.

```bash
python3 get_imgs.py
```

- `notebooks/01_eda_data_preparation.ipynb`: exploratory data analysis and data preparation (i.e., data cleansing and train-val split).

- `notebooks/02_model_development.ipynb`: process of model development.
> To download the `model.h5` file that contains the convnet architecture and trained weights, run `download_model.py` from a terminal opened in the scripts directory.

```bash
python3 download_model.py
```

- `notebooks/03_model_evaluation.ipynb`: performance evaluation of the classifier on the validation set.


## Streamlit app

The app folder contains the source code of a Streamlit web application that let's you easily interact with the model. To launch the app, navigate to the app directory from a terminal and run:

```bash
streamlit run streamlit_app.py
```
