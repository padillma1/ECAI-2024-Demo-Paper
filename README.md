# ECAI-2024-Demo-Paper
The objective of this project is to extend the existing federated learning benchmark and dataset suite FLamby (https://github.com/owkin/FLamby), specifically for the UCI heart disease dataset (https://archive.ics.uci.edu/dataset/45/heart+disease). We do this by running the centralized dataset on several binary classification models, which are hyperparameter tuned and run on 10 different seeds, and federate the best performers. We compare our results to the results obtained by the default model used in FLamby (logistic regression, using a learning rate of 0.001 and batch size of 4).

A secondary objective of this work is to address the misuse of duplicated data by other researchers in the heart disease classification task. Several papers use a modified version of the Cleveland dataset, obtained on Kaggle (https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset), which contains more than 700 duplicated data points, resulting in highly inflated accuracies. The results obtained by FLamby and in this work use the unmodified dataset, and we only perform standard preprocessing such as removing missing values and binarizing the labels. 

The most challenging part was federating the SVM model because there is no PyTorch SVM model that we can drop into the code (PyTorch makes for simple and flexible optimization of the models) like we were able to do with the one and two-layer neural networks. 

Demo video link: https://youtu.be/QSfnFeUSL1k?si=kb1r9LZqqSUZGBUj


