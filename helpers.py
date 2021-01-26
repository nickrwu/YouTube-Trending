# Importing modules
import pandas as pd
import numpy as np
import datetime as dt

from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

# Function to Load Dataframe
def load_df(filename):
    """
    Loads data frame based on filename parameter
    """
    df = pd.read_csv(filename)
    # Set seed for reproducibility
    np.random.seed(0)

    return df

# Feature Engineering & Preprocessing Data
def featureEng(df):
    """
    Creates new variables from existing data
    """
    # Adding Like/Dislike Ratio Column
    df['likeRatio'] = (df['likes']-df['dislikes'])/(df['likes']+df['dislikes'])

    # Dropping rows with disabled comments and ratings
    df.drop(df[(df['comment_count'] == 0) | (df['ratings_disabled']) | (df['view_count'] == 0)].index,
    inplace=True)
    
    # Adding Log of Ratings, Views, and Comments (Eliminate Skew)
    df['likes_log'] = np.log(df['likes'])
    df['views_log'] = np.log(df['view_count'])
    df['dislikes_log'] = np.log(df['dislikes'])
    df['comment_log'] = np.log(df['comment_count'])

    # Changing the 'publishedAt' and 'trending_date' type from string to datetime type
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], format='%Y-%m-%d').dt.tz_localize(None)
    df['new_date_published'] = df['publishedAt'].dt.date
    df['trending_date'] = pd.to_datetime(df['trending_date'], format="%y.%d.%m")
    df['new_date_trending'] = df['trending_date'].dt.date
    df['days_lapse'] = (df['new_date_trending'] - df['new_date_published'])/dt.timedelta(days=1)

    # Breaking down 'duration' into Hour, Minutes, and Seconds
    df['durationHr'] = df['duration'].str.extract('(\d+)H').fillna(0).astype(int)
    df['durationMin'] = df['duration'].str.extract('(\d+)M').fillna(0).astype(int)
    df['durationSec'] = df['duration'].str.extract('M(\d+)S').fillna(0).astype(int)

    # Adding 'titleLength' Column
    df['titleLength'] = df['title'].apply(lambda x: len(str(x)))

    # Adding 'tagCount' Column
    df.loc[df['tags'].str.count("\|") != 0, 'tagCount'] = df['tags'].str.count("\|") + 1
    df.loc[df['tags'].str.count("\|") == 0, 'tagCount'] = 0
    df['tagCount'] = df['tagCount'].astype(int)
    return df

def preprocess(df):
    # Dropping duplicate rows
    df.drop_duplicates(subset=['video_id'], keep='last', ignore_index=True)
    
    # Dropping unneeded columns
    df.drop(columns=['country', 'view_count', 'comment_count', 'likes', 'dislikes',
    'trending_date', 'publishedAt', 'channelTitle', 'channelId', 'title', 'description', 'video_id', 'tags', 'thumbnail_link', 'new_date_published',
    'new_date_trending', 'comments_disabled', 'duration',
    'ratings_disabled'], axis=0, inplace=True)
    
    # Drop missing values
    df.dropna()

    return df

def findOutliers(col):
    outliers = []
    Q1 = col.quantile(0.25)
    Q3 = col.quantile(0.75)
    IQR = Q3 - Q1

    lowerLim = Q1 - (1.5*IQR)
    upperLim = Q3 - (1.5*IQR)

    for out1 in col:
        if out1 > upperLim or out1 < lowerLim:
            outliers.append(out1)

    return np.array(outliers)

def scaling(X,y):
    scaler = ColumnTransformer([
            ('standardize', StandardScaler(), 
            ['tagCount','titleLength','comment_log','dislikes_log', 'views_log'])
        ])
    X[['tagCount','titleLength','comment_log','dislikes_log', 'views_log']] = scaler.fit_transform(X,y)

