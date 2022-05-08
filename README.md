# MTG Basic Lands Classifier

A Magic: The Gathering basic lands classifier.

The model receives an artwork as input and predicts whether it's a Plains, Island, Swamp, Mountain or Forest.

![alt text](https://github.com/jansaldo/MTG-Basic-Lands-Classifier/blob/main/sample_preds.gif?raw=true "Sample predictions")
 
This repository contains the code that was used to develop the convolutional neural network using [TensorFlow](https://www.tensorflow.org/). Data was collected using the [Scryfall API](https://scryfall.com/docs/api).

The machine learning workflow can be followed with these notebooks:

- `notebooks/00_fetch_data.ipynb`: consumption of [Scryfall API](https://scryfall.com/docs/api) in order to fetch the available images of basic lands which are used to develop the classification model.
> To get the same dataset that was used throughout this project, run `scripts/get_imgs.py` from a terminal instead of running this notebook. Image files weren't uploaded to GitHub to keep the repository size small.

- `notebooks/01_eda_data_preparation.ipynb`: exploratoy data analysis and data preparation (i.e., data cleansing and train-val-test split).

- `notebooks/02_model_development.ipynb`: process of model development.
> To download the `model.h5` file that contains the convnet architecture and trained weights, run `scripts/download_model.py` from a terminal.

- `notebooks/03_model_evaluation.ipynb`: performance evaluation of the classifier on the validation set.