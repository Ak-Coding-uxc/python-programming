from nltk import word_tokenize , pos_tag

text = "I love NLP."

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print(tags)