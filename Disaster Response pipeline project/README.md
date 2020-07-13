# Disaster Response Pipeline Project

### Project Description
In this project, we have build a model to classify messages that are sent during disasters. There are 36 pre-defined categories, and examples of these categories include Aid Related, Medical Help, Search And Rescue, etc. By classifying these messages, we can allow these messages to be sent to the appropriate disaster relief agency acccording to the catagory. This project involves the building of basic ETL pipeline and Machine Learning pipeline to complete  the task. This is also a multi-label classification task, since a message can belong to one or more categories. We will be working with a data set provided by Figure Eight containing real messages that were sent during disaster events.At the end,this project contains a web app where we can input a message and get classification results.
https://github.com/AnkanPatel/Udacity-Data-Science-nanodegree-program-/blob/master/Disaster%20Response%20pipeline%20project/WebApp.png


### File Description
    disaster_response_pipeline
           1.app
               1.1 templates
                   1.1.1 go.html
                   1.1.2 master.html
               1.2 run.py
           2.data
               2.1 disaster_message.csv
               2.2 disaster_categories.csv
               2.3 DisasterResponse.db
               2.4 process_data.py
           3.models
               3.1 classifier.pkl
               3.2 train_classifier.py
           4.Preparation
               4.1 categories.csv
               4.2 ETL Pipeline Preparation.ipynb
               4.3 ETL_Preparation.db
               4.4 messages.csv
               4.5 ML Pipeline Preparation.ipynb
               4.6 README
           5.README

### Installation of libraries
We require  Python 3 with libraries of numpy, pandas, sqlalchemy, re, NLTK, pickle, Sklearn, plotly and flask libraries.

### File Descriptions
App folder including the templates folder and "run.py" for the web application
Data folder containing "DisasterResponse.db", "disaster_categories.csv", "disaster_messages.csv" and "process_data.py" for data cleaning and transfering.
Models folder including "classifier.pkl" and "train_classifier.py" for the Machine Learning model.
README file
Preparation folder containing 6 different files, which were used for the project building. (Please note: this folder is not necessary for this project to run.)

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


