from textblob import TextBlob
#import nltk
#also had to downlaod 'patch'
#nltk.download('averaged_perceptron_tagger')
wiki = TextBlob(" I hate violence")

#to check parts of speech
print(wiki.tags)

#tokenization
print(wiki.words)

#checking the polarity
print(wiki.sentiment.polarity)