from sklearn.feature_extraction.text import TfidfVectorizer

text = ["I love cricket" , "His name is Cricket" , "He also love Football"]

tfidf = TfidfVectorizer()

X = tfidf.fit_transform(text)

print(tfidf.get_feature_names_out())
print(X.toarray())

