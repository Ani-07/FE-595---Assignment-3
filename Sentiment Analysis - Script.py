# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:13:36 2020

@author: Anirudh Raghavan
"""

# Objective - Perform sentiment analysis on purpose of companies to determine 
# top 10 and worst 10 companies

from vaderSentiment.vaderSentiment \
import SentimentIntensityAnalyzer

import pandas as pd

# Import data

NLP_data = pd.read_csv("NLP Data.csv")

# Setup sentiment analyzer

# Our ranking will be based on compound sentiment so we shall extract only the
# compound score

analyser = SentimentIntensityAnalyzer()

def sentiment_analysis(text):
        score  = analyser.polarity_scores(text)
        compound_score = score["compound"]
        return compound_score


def Purpose_sentiment (dataframe):
    purpose = list(NLP_data.iloc[:,1])
    sentiment = list(map(sentiment_analysis,purpose))
    NLP_data['Sentiment_Score'] = sentiment
    NLP_data.sort_values(by=['Sentiment_Score'], inplace=True, ascending=False)
    return NLP_data

if __name__ == "__main__":
    NLP_data = Purpose_sentiment(NLP_data)
    top_10 = NLP_data.nlargest(10,['Sentiment_Score'])
    top_10.to_csv("NLP - Top 10.csv",index=False)
    last_10 = NLP_data.nsmallest(10,['Sentiment_Score'])
    last_10.to_csv("NLP - Last 10.csv",index=False)

