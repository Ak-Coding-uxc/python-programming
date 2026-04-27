""" 
Claude notes:- https://claude.ai/share/de5a8bbd-0b98-464b-829f-e62f2df79052
ChatGPT notes:- https://chatgpt.com/share/69909259-e4b0-8012-9db7-78ca2f75c53d
 """

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
""" This are like a brains to nlp need to install """

text = "The students are studying NLP. They have been waiting in the lab for 1 hour!"

tokens = word_tokenize(text.lower())

stop_words = stopwords.words('english')
filtered_tokens = [w for w in tokens if w not in stop_words and w.isalnum()]
""" 
# i used w.isalnum() to remove punctuations and special symbols
# Punctuation marks are symbols used in writing to separate sentences and clarify meaning (e.g., . , ? !)
# special symbols are non-alphanumeric characters used for technical or mathematical purposes (e.g., @ # $ %) 
"""

lemmatizer = WordNetLemmatizer()
lemmatized_output = [lemmatizer.lemmatize(word) for word in filtered_tokens]
"""Improved Version of lemmatizer get POS(Parts of Speech) Tag :- Apply grammatical category like verb , subject etc"""



print("Original: ",text)
print("Tokens: ",tokens)
print("Cleaned & Lemmatized: ",lemmatized_output)

