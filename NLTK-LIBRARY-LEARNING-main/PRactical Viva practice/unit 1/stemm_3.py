# rt -> tokenization -> lowercaseing -> stopword removal -> stemming / lemmatization -> vectorization

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer # this is class

text = "Separate school shootings in Siverek and in Onikişubat, Turkey, leave 12 people dead and 35 others injured."

words = word_tokenize(text)
words = [w.lower() for w in words]

stop_words = stopwords.words('english')

filtered = [w for w in words if w not in stop_words]

stemmer = PorterStemmer()

stem_Filterd_Tokens = [stemmer.stem(w) for w in filtered]

print("Original Text:- ",text)
print("\nTokens = ",words)
print("\nFilter Text = ",filtered)
print("\nStem Words = ", stem_Filterd_Tokens)



