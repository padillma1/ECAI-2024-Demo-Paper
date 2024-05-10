# ECAI-2024-Demo-Paper
The objective of this project is to extend the existing federated learning benchmark and dataset suite FLamby (https://github.com/owkin/FLamby), specifically for the UCI heart disease dataset (https://archive.ics.uci.edu/dataset/45/heart+disease). We do this by running the centralized dataset on several binary classification models, which are hyperparameter tuned and run on 10 different seeds, and federate the best performers. We compare our results to the results obtained by the default model used in FLamby (logistic regression, using a learning rate of 0.001 and batch size of 4).

A secondary objective of this work is to address the misuse of duplicated data by other researchers in the heart disease classification task. Several papers use a modified version of the Cleveland dataset, obtained on Kaggle (https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset), which contains more than 700 duplicated data points, resulting in highly inflated accuracies. The results obtained by FLamby and in this work use the unmodified dataset, and we only perform standard preprocessing such as removing missing values and binarizing the labels. 

The most challenging part was federating the SVM model because there is no PyTorch SVM model that we can drop into the code (PyTorch makes for simple and flexible optimization of the models) like we were able to do with the one and two-layer neural networks. 

Demo video link: https://youtu.be/QSfnFeUSL1k?si=kb1r9LZqqSUZGBUj

Requirements
-Have at least 200 MB free space to download and install the FLamby benchmark, including the heart disease dataset
-Have Python and Git installed 
-Recommended to use Anaconda for easy installation
-Per the FLamby github, perform the following terminal commands (one by one) to download and install the repository for the heart disease dataset
o	git clone https://github.com/owkin/FLamby.git
o	cd FLamby
o	make enable=heart install
o	conda activate flamby 
o	make update
-If “make” command is not available on your machine, run this instead
o	git clone https://github.com/owkin/FLamby.git
o	cd FLamby
o	conda env create -f environment.yml
o	conda activate flamby
o	pip install -e .[heart]
-Download the heart disease dataset 
o	cd flamby/datasets/fed_heart_disease/dataset_creation_scripts
o	python download.py --output-folder ./heart_disease_dataset
-Once the dataset has been installed, check to see if the benchmark code runs
o	cd flamby/benchmarks
o	python fed_benchmark.py --seed 42 -cfp ../config_heart_disease.json
-Replace the “model.py”, “loss.py”, and “metric.py” in \User\FLamby\flamby\datasets\fed_heart_disease with the ones found here:  padillma1/ECAI-2024-Demo-Paper (github.com)
-Do the same for “benchmark_utlils.py” in \User\FLamby\flamby\benchmarks

