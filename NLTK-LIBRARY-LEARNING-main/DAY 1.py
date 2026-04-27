""" 
NLTK (Natural Language Toolkit)
👉 Python ki library hai
👉 Jo computer ko human language (English text) samajhne mein help karti hai
 """
# .tokenize is module and word_tokenize is function 
# tokenize => meaningful small small parts(word, sentences) of text
# chat gpt => https://chatgpt.com/share/69909259-e4b0-8012-9db7-78ca2f75c53d
""" 
from nltk.tokenize import word_tokenize

text = "I am a man!"
# t1 = text.split()
# print(t1)
token = word_tokenize(text) # text split in small small parts
print(token)
"""

""" from nltk.tokenize import sent_tokenize
text = "I am 21 years old! What you want from me ?"
sentences = sent_tokenize(text)
print(sentences)
 """

from nltk.tokenize import sent_tokenize

text = "Python is easy, but NLP is powerful!"
token = sent_tokenize(text)
print(token)