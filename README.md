# Kaggle_analysis_crime.vancouver

This is a statistical analysis of criminal activities in vancouver dataset available from kaggle.
Also, different machine learning approaches are being applied to the dataset for prediction modelling. (Under-Development)

**Link to dataset: ** https://www.kaggle.com/wosaku/crime-in-vancouver/data

## Statistical Analysis

**Files to know**

**data_analysis.py**

This files provides all the necessary functions to generate initial results from the dataset.

Running the analysis function inside data_analysis.py generates the different types of columns and the different types of criminal activities reported.

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2000-55-57.png)

It also shows the number of Neighborhoods and their names

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2000-56-30.png)

This shows the per type count values for th various criminal activities reported.

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2000-56-57.png)

This also provides an interactive way to input the year and month to generate month-specific criminal activities reported.
![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2000-57-19.png)

The distribution of crimes per day is given here. It is a normal distribution with an outlier over 600 and has a mean at around 95

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/dist_crimes_per_day.png)

The crime_time_series analysis tries to demonstrate how the number of criminal activities varied within 2STDs

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/time_series_analysis.png)


## Predictive Modelling
Here, we are introduced a new column named "Classification" which is set to +1 if the criminal activity occured via Vehicle Collision else everything else is set to -1. We ran the ML models over 50,000 data-points due to memory constraints on our computing systems.

**Logistic Regression**

Our main reason to apply logistic regression over linear regression is to regress over a categorical outcome(+1,-1)

_Results_

ROC Curve:

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/logreg_plot.png)

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2021-05-29.png)

**Decision Tree**

We decide to run the decision tree technique which splits the dataset based on feature selection by calculating the entropy and information gain

![alt text](https://github.com/Arghyadatta/kaggle_analysis_crime.vancouver/blob/master/plots/Screenshot%20from%202018-03-02%2021-05-58.png)
