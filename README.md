# Starbucks Capstone Challenge
Udacity Capstone Project in Data Scientist Nanodegree

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

All relevant libraries are named within the notebook and all of them should be available through anaconda or pip. The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

This is the capstone project the Data Scientist Nanodegree at Udacity. The dataset at hand is provided by Udacity and contains simulated data from the Starbucks rewards app. The goal of this project is, therefore, to gain insights to help Starbucks optimize its promotion strategy with this app. 

## File Descriptions <a name="files"></a>

The notebook available here showcases work related to the goal mentioned above.  

The data is consists of three JSON files stored in the `data` directory:
- `portfolio.json` - containing offer ids and meta data about each offer (duration, type, etc.)
- `profile.json` - demographic data for each customer
- `transcript.json` - records for transactions, offers received, offers viewed, and offers completed

The schema is as follows:

`portfolio.json`
- id (string) - offer id
- offer_type (string) - the type of offer ie BOGO, discount, informational
- difficulty (int) - the minimum required to spend to complete an offer
- reward (int) - the reward is given for completing an offer
- duration (int) - time for the offer to be open, in days
- channels (list of strings)

`profile.json`
- age (int) - age of the customer
- became_member_on (int) - the date when customer created an app account
- gender (str) - gender of the customer (note some entries contain 'O' for other rather than M or F)
- id (str) - customer id
- income (float) - customer's income

`transcript.json`
- event (str) - record description (ie transaction, offer received, offer viewed, etc.)
- person (str) - customer id
- time (int) - time in hours since the start of the test. The data begins at time t=0
- value - (dict of strings) - either an offer id or transaction amount depending on the record

Directory `img` contains visualisations used for the blog post.
The `src` directory contains a python script used for unnesting the transcript data.
Directory `model` contains a tuned version of the Gradient Boosting Regressor.


## Results<a name="results"></a>

The main findings of this project can be found [here](https://medium.com).

Based on the transcript records, this project focuses on thoroughly analyzing purchasing decisions and how promotional offers, user behavior, and additional demographic factors influence these decisions. To do so, I train tree-based regression models to predict a user's profit per offer type and analyze their characteristics to derive recommended actions for Starbucks. 

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

For the data credit goes to Udacity and Starbucks for providing it. Otherwise, feel free to use the code as you like.
