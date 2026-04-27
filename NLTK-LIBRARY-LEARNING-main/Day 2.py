# 15 FEB 2025
"""
Today Topic is Stopwords(text se bekar words bahar nikalna)
Stopwords = aise common words jo meaning mein zyada help nahi karte
Examples:- is, am, are, the, a, an, in, on, at, to, of
examples:- I am learning NLP
    imp words => learning NLP
    I, am 👉 Ye stopwords hain
 """

# without libray
""" text = "I am Learning NLP"
token = text.split()
print(token)
stopwords = ["I", "am"]
filtered = [w for w in token if w not in stopwords]
print(filtered) """
""" 
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

from nltk.tokenize import word_tokenize

text =" I am good in Maths. But I am bad in English"

words = word_tokenize(text) 

filtered_words = [w for w in words if w.lower() not in stop_words]

print(filtered_words)
 """


""" from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = stopwords.words('english')

text = "My name is Aman. What is your name?"
words = word_tokenize(text)
filtered = [w for w in words if w.lower() not in stop_words]

print(filtered)
 """

# Practice
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Now i am learning NLP library in Python. What to learn next?"
token = word_tokenize(text)

stop_words = stopwords.words('english')

result = [w for w in token if w.lower() not in stop_words ] 

print(result)
