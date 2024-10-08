# README - Neural Networks in Cryptanalysis: Investigating DES Encryption
---
## Overview

- This repository contains the research paper "Investigating The Effectiveness of Neural Networks in Cryptanalysis" and its accompanying source code. The project explores the potential of using neural networks, specifically multilayer perceptrons, in the cryptanalysis of symmetric encryptions, focusing on the Data Encryption Standard (DES).
---
## Contents
1. `Neural Networks in Cryptanalysis Investigation.pdf`: The full research paper detailing the investigation, methodology, and results.
2. `neural_network_on_des.ipynb`: Python script for training and analyzing the neural network model.
3. `dictionary_filtering.py`: Script for filtering and preparing the dictionary dataset.
4. `des_encryption_dictionary.py`: Implementation of DES encryption for the dictionary dataset.
5. `des_encryption_algorithm.py`: General DES encryption algorithm implementation.
---
## Key Features
- Implementation of a neural network for cryptanalysis of DES encryption
- Comparison of performance on dictionary words vs. random bit sequences
- Detailed analysis of model performance using various metrics
---
## Requirements
- Python 3.x
- Libraries: numpy, pandas, scikit-learn, seaborn, matplotlib, pyDes
---
## Usage
1. Ensure all required libraries are installed.
2. Run `dictionary_filtering.py` to prepare the dictionary dataset. 
3. Use `des_encryption_dictionary.py` and `des_encryption_algorithm.py` to generate encrypted data.
4. Execute `neural_network_on_des.ipynb` to train the model and analyze results.
5. Obtain `predictor.joblib` as a pickle file to use the neural network for decryption.
---
## Results

- Achieved approximately 70% accuracy in decryption which seems impressive however even one incorret bit would mean that the DES decrypted word would be illegible.
- The investigation demonstrates that neural networks show potential in cryptanalysis, particularly when the original text is from an English dictionary. However, the model struggles with completely random bit sequences, highlighting the limitations of this approach.
---
## Future Work
- Explore more advanced neural network architectures
- Investigate application to other encryption algorithms
- Improve model performance for random bit sequences

## Author
Jerry Wu

## Acknowledgements
Special thanks to American School of Milan and specifically Dr.Stephen Reiach for the opportunity to research on the project.
