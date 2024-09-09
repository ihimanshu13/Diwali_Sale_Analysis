# -*- coding: utf-8 -*-
"""Movie_Recommendation_system.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1P_UpnU4na9WhKdBmGHZqYq_Y0sMmSg6g

**Movie Recommendation System**

**Import library**
"""

import pandas as pd

import numpy as np

df = pd.read_csv(r"https://raw.githubusercontent.com/YBI-Foundation/Dataset/main/Movies%20Recommendation.csv")

df.head()

df.info()

df.shape

df.columns

"""Get Feature Selection"""

df_features =df[['Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' ' + df_features['Movie_Tagline'] + ' ' + df_features['Movie_Cast'] + ' ' + df_features['Movie_Director']

x.shape

"""**Get Featured Text Conversion To Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf =TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""**Get Similarity Scores using Cosine SImilarity**"""

from sklearn.metrics.pairwise import cosine_similarity

similarity_score= cosine_similarity(x)

similarity_score

similarity_score.shape

"""**Get Movie name as input from User and validated for closest setting**"""

favourite_Movie_Name =input('Enter your favourite name: ')

All_Movies_Title_List= df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(favourite_Movie_Name,All_Movies_Title_List)
print(Movie_Recommendation)

close_Match = Movie_Recommendation[0]
print(close_Match)

Index_of_close_Match_Movie = df[df.Movie_Title == close_Match]['Movie_ID'].values[0]
print(Index_of_close_Match_Movie)

"""Getting a list of similar Movies"""

Recommendation_score = list(enumerate(similarity_score[Index_of_close_Match_Movie]))
print(Recommendation_score)

len(Recommendation_score)

"""Get all movies sort based on Recommendation score wrt to favourite movies"""

#sorting the movies based on similarity score
sorted_similar_movies = sorted(Recommendation_score, key = lambda x:x[1], reverse=True)
print(sorted_similar_movies )

"""Print the names of similar movies based on index"""

print("Top 30 movies suggested for you :\n")

i=1

for movie in sorted_similar_movies:
  index= movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i,'.',title_from_index)
    i+=1