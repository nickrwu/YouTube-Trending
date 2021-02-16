## YouTube Trending Project
![alt text](https://github.com/nickrwu/YouTube-Trending/blob/master/youtube-logo.png)
### [Project Presentation Link](https://drive.google.com/file/d/1uf0sMXe4I9CMLMrsC8EncS9I0Y35aHlg/view?usp=sharing)

Analyzing data from the YouTube trending page in the US using data agreggated over October, December, and January in 2020 and 2021

Goal: 
* To understand common characteristics of trending videos in the US

* Use this knowledge to build predictive models

* To predict engagement (likes and views) on a video in the US

### Table of Contents:
* 1.Exploratory Data Analysis
    * 1.1 Data Analysis
        * 1.1.1 Raw Data Information
    * 1.2 Feature Engineering
        * 1.2.1 Like/Dislike Ratio
        * 1.2.2 Log of Ratings, Views, and Comment Counts
        * 1.2.3 Days Lapsed
        * 1.2.4 Duration Columns
        * 1.2.5 Title Length
        * 1.2.6 Tag Count
    * 1.3 Variable Analysis
    * 1.4 Heat Map
    * 1.5 Plotting Distributions
    * 1.6 Category Analysis
        * 1.6.1 Graphing video counts by category
    * 1.7 Correlation Matrix
* 2.Cleaning
    * 2.1 Preprocessing Data
        * 2.1.1 Drop Duplicate Rows
        * 2.1.2 Drop Columns
        * 2.1.3 Handling Missing Data
    * 2.2 Post-Processed Data
        * 2.2.1 Column Information
        * 2.2.2 Exporting Curated Data
    * 2.3 Export Cleaned Data w/ All Columns
* 3.Modeling
    * 3.1 Predicting Likes
        * 3.1.1 Pre-processing Data
            * 3.1.1.1 Train-Test Split (80:20)
            * 3.1.1.2 Initializing Pre-processing Pipeline
        * 3.1.2 Hyperparameter Tuning (Gridsearch)
        * 3.1.3 Regressors
            * 3.1.3.1 Linear Regression
            * 3.1.3.2 Random Forest
            * 3.1.3.3 XGBoost
        * 3.1.4 Random Forest
            * 3.1.4.1 Feature Importance
        * 3.1.5 Likes Evaluation
    * 3.2 Predicting Views
        * 3.2.1 Pre-processing Data
            * 3.2.1.1 Train-Test Split (80:20)
            * 3.2.1.2 Initializing Pre-processing Pipeline
        * 3.2.2 Hyperparameter Tuning (Gridsearch)
        * 3.2.3 Regressors
            * 3.2.3.1 Linear Regression
            * 3.2.3.2 Random Forest
            * 3.2.3.3 XGBoost
        * 3.2.4 Random Forest
            * 3.2.4.1 Feature Importance
        * 3.2.5 Views Evaluation
