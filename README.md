# Personality Predictor

This is a personality predicitor trained on kaggle [MBTI dataset](https://www.kaggle.com/datasets/datasnaek/mbti-type). You can input post of a person and it can perdict the personality of that person according to Myers-briggs.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bhatir16/mbti_project.git

2. Navigate to the directory

   ```bash
   cd mbti_project

3. To run this project you should have python and Jupyter notebook installed in your system.

4. Install the requirements using

   ```bash
   pip install -r requirements.txt

5. Paste dataset mbti_1.csv that can be downloaded from kaggle(link above) into the directory

## Usage

1. Run your jupyter notebook server and run final.ipynb.
2. Open predict.py in any text editor and paste the post in the variable `new_post`.
3. Close your notebook, text editor and open the directory in python shell.
4. Now type `python predict.py` to predict the personality.
