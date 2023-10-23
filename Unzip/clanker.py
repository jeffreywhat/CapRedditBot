import nltk
#import sklearn
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
from io import StringIO
from profanity_check import predict, predict_prob

n = 30000
with open('RC_2023-01.csv') as f:
    head = ''.join(f.readlines(n))
    
df = pd.read_csv(StringIO(head))
print(df)

analyzer = SentimentIntensityAnalyzer()
body = list(df['body'])


data = []
prof = []
for sentence in body:
    sentiment_score = analyzer.polarity_scores(" ".join(sentence))
    profanity_score = predict_prob(" ".join(sentence))
    data.append(sentiment_score['compound'])
    prof.append(profanity_score)


df['profanity'] = prof
df['sentiment'] = data

clean_sent_prof = df[(df['profanity'] > 0.3) & (df['sentiment'] < -0.8)]
low_sent_prof = df[(df['profanity'] <= 0.3) | (df['sentiment'] >= -0.8)]

print(clean_sent_prof.head())
print(low_sent_prof.head())

print(clean_sent_prof['body'])
print(low_sent_prof['body'])

clean_sent_prof.to_csv(index=False)


