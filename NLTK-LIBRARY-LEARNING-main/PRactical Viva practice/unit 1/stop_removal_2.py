from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.corpus import stopwords

text = "I love NLP. But I hate theory subjects "

# words = word_tokenize(text.lower())# convert in lower case is very important here

words = word_tokenize(text)
words = [w.lower() for w in words]

stop_words = stopwords.words('english')

filtered = [w for w in words if w not in stop_words]

print(f"Words Tokens = {words}\nfiltered sentences = {filtered}")

# convert in lower case