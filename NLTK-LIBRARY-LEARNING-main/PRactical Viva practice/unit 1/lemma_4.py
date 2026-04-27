from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer # this is class

text = "Separate school shootings in Siverek and in Onikişubat, Turkey, leave 12 people dead and 35 others injured."

words = word_tokenize(text)
words = [w.lower() for w in words]

stop_words = stopwords.words('english')

filtered = [w for w in words if w not in stop_words]

lemma = WordNetLemmatizer()

lemma_Filterd_Tokens = [lemma.lemmatize(w) for w in filtered] # important part

print("Original Text:- ",text)
print("\nTokens = ",words)
print("\nFilter Text = ",filtered)
print("\nStem Words = ", lemma_Filterd_Tokens)


# here focus on lemmatize thing , not used + d.