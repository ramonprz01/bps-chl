# Sypht Challenge

This repo contains the set of challenges given to a software engineer (sort of ML engineer) candidate at Sypht. There is only one required problem, the first one, and three optional ones. Each of the completed ones will be in their respective folder alongside a README file with the problem prompt and additional info regarding how to run it.


## Content

1. `problem_0`: This folder contains a Python CLI app with a date calculator.
2. `problem_1`: This folder contains a Python with an app that allows you to upload invoices to Sypht using their API, it then displays the invoice and it shows you the content captured in JSON format.


## Setup

To run the app contained in `problem_1` you will need to set up a python environment either with the Anaconda distribution (preffered), `virtualenv`, or `pipenv`. Conversely, you could bypass setting up an environment with a Python>=3.7 and by installing the `panel` package with `pip install panel` (not recommended).

1. Clone the repo
```sh
git clone git@github.com:ramonprz01/bps-chl.git
```

2. Create the environment

```sh  

# if you have conda  
conda env create -f environment.yml

# if you don't have conda crete an env first
python -m venv my_challenge

# then activate it
source myvenv/bin/my_challenge

# install the required packages
python -m pip install -r requirements.txt
```

3. Navigate to problem 0 or 1 and run `python app1.py or app2.py`
