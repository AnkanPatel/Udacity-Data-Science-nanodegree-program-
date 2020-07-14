## Udacity Data Science Nanodegree Capstone Project
### Capstone project:
Starbucks Capstone Challenge: Using Starbucks app user data to predict effective offers

### 1.Installations
we have used python3 and libraries such as:

*pandas
*numpy
*math
*json
*time
*sklearn.model_selection (GridSearchCV)
*matplotlib
*seaborn
*sklearn.model_selection (train_test_split module)
*sklearn.preprocessing (StandardScaler, PolynomialFeatures)
*from sklearn.tree (DecisionTreeClassifier,DecisionTreeRegressor)
*sklearn.ensemble (RandomForestClassifier)
*sklearn.metrics (mean_squared_error,classification_report)
*sklearn.linear_model (Ridge)
 
### 2.Business Questions:
As a part of the final project in udacity data science nanodegree program i have done this starbucks app user data to predict effective offers poroject.
In this project, I have tried to answer 2 business questions:

1. An effective offer on the Starbucks app depends on which drivers?
2. Could  whether a user would take up an offer or not be predicted using the data provided?
To answer the above 2 questions, I have created a scenario which contains 3 models depending upon the  three offer types.
The three offer types are:Discount (discount with purchase),Informational (provides information about products), Buy One Get One Free (BOGO).

### Summary:
If we discuss about Question 1,then the feature importance given by all the three different models that we are using were from where we found that the tenure of a member is the biggest predictor of the effectiveness of an offer.
On performing further operations we would be able to calculate the number of average tenure days as a result of an effective BOGO offer.

If we discuss aboutr Question 2,I have uesd 3 different models to predict the effectiveness of each offer type and i got a good accuracy value for 2 of the models
(87.35% for discount and 82.83% for BOGO), while in other model there is a slightly accurate performance that is in informational offers (75.3%). 
However, I think 75% as acceptable in a business setting, as for informational offers.
Meanwhile, an 80% and above accuracy in a business setting is better to show offers to people.

### 3.File Descriptions
This repo contains 4 files-

1.Starbucks_Capstone_notebook.ipynb

2-data : data.zip(portfolio.json, profile.json and transcript.json)(as the size of ine of the file is bigger so i have used it as a zip)

3-images(pic-1,pic-2)


You can find my blog <a href="https://medium.com/@ankanpatel23/analyzing-starbucks-offers-data-35927832e0f1">here</a>
