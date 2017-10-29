#!/usr/bin/env python3
# _*_ coding: utf-16 _*_

# Quiz Question 50

import numpy as np
import pandas as pd

def read_data_to_dfs():
    uDheaders = ["user id", "item id", "rating", "timestamp"]
    uDdf = pd.read_table("./Quiz/ml-100k/u.data", sep='\t', names=uDheaders)
    
    uUheaders = ["user id", "age", "gender", "occupation", "zip code"]
    uUdf = pd.read_table("./Quiz/ml-100k/u.user", sep='|', names=uUheaders)

    uIheaders = ["movie id", "movie title", "release date", "video release date", "IMDb URL", "unknown", "Action", \
                 "Adventure", "Animation", "Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", \
                 "Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", "War", "Western"]
    
    uIdf = pd.read_table("./Quiz/ml-100k/u.item", sep='|', names=uIheaders, encoding = "ISO-8859-1")
    
    return (uDdf, uUdf, uIdf)

if __name__ == "__main__":
    uDdf, uUdf, uIdf = read_data_to_dfs()
    
#     print(uDdf.head())
#     print(uUdf.head())
#     print(uIdf.head())
    
    genderRatingdf = pd.merge(uDdf, uUdf,  on = "user id", how = "inner")
    
    print(genderRatingdf.groupby('gender').std().rating)
    
#     print(genderRatingdf.head())

