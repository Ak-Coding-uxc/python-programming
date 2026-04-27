from sklearn.feature_extraction.text import CountVectorizer

docs = ['I love cricket', 'I love football', 'cricket is great']

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(docs)

print(vectorizer.get_feature_names_out()) 
print(X.toarray())


# output
"""
['cricket' 'football' 'great' 'is' 'love']
[[1 0 0 0 1]
 [0 1 0 0 1]
 [1 0 1 1 0]]
"""