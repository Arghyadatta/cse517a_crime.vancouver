# Kaggle_analysis_crime.vancouver

This is a statistical analysis of crime in vancouver dataset available from kaggle.
Also, different machine learning approaches are being applied to the dataset for prediction modelling. (Under-Development)

**Link to dataset: ** https://www.kaggle.com/wosaku/crime-in-vancouver/data

**Files to know**

_data_analysis.py_

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


