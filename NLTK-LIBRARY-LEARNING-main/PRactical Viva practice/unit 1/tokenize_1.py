from nltk.tokenize import word_tokenize , sent_tokenize


text = "I love NLP. But I hate theory subjects "

words = word_tokenize(text)

sents = sent_tokenize(text)

print(f"Words Tokens = {words} \nSents Tokens = {sents}")











