import nltk
import pyfiglet 
import pandas as pd
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
from textblob import TextBlob

font = pyfiglet.figlet_format("Sentiment analysis", font = "bulbhead")
print(font)

def sentiment_label(result):
    if result > 0 and result < 0.4:
        return "Slightly Positive"
    elif result > 0.5:
        return "Positive"
    elif result < 0 and result > -0.4:
        return "slightly Negative"
    elif result < -0.5:
        return "Negative"
    elif result == 0:
        return "Neutral"

m1 = input("Hi how are you ?  : ")
name = input("May i know your name ? : ")
m2 = input(f"How was your day ? {name}: ")
m3 = input("describe about your day today ? :")
print(f"Thank you for your time {name}")

data = {
    'text' : [m1, m2, m3]
}
df = pd.DataFrame(data)
text = ', '.join(df['text'].values)

blob = TextBlob(text)

# Perform sentiment analysis
sentiment_score = blob.sentiment.polarity

sentiment_result = sentiment_label(sentiment_score)
print('--------------------------------')
print("\n\nprediction score : " + str(sentiment_score))
print("your sentiment score is "+sentiment_result)
print('--------------------------------')

