# 15 FEB 2026
# Today topic is Stemming
# Stemming = word ko uske root (base) form mein laana
# example:- running = run , coming = come(base form) , runs = run

""" from nltk.stem import PorterStemmer

stemmer = PorterStemmer() # this line created stemmer object

words = ['running', 'runs', 'studies' , 'runner', 'played' , 'playing']
stemmed_words = [stemmer.stem(word) for word in words]

print(stemmed_words) """

""" 
👉 Stemming meaning check nahi karta
👉 Bas mechanically word cut karta hai 
"""
# practice
""" 
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ['cats', 'catlike', 'studying', 'studies', 'studied']

stemmer_words = [stemmer.stem(word) for word in words]

print(stemmer_words)
['cat', 'catlik', 'studi', 'studi', 'studi']
 """


# Practice

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer # to make stemmer object that convert word into base form

# step 1 => tokenization
text = "Lets play in the desert and playing with childrens in the woods with eating potatoes"
words = word_tokenize(text)
print("Word Tokenization:- ")
print(words)
print()

# step 2 => stopwords removal
stop_words = stopwords.words('english')
filtered_result = [w for w in words if w.lower() not in stop_words]
print("Filtered Results:-")
print(filtered_result)
print()

#step 3 => Stemming
stemmer = PorterStemmer()
stemmer_words = [stemmer.stem(word) for word in filtered_result]
print("Result of applying Stemmer in filtered result")
print(stemmer_words)


