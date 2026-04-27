# 17 FEB 2026
# Today topic is Lemmatization
# Lemmatization = word ko uske “dictionary-correct base form (lemma)” mein laana
# examples:- running → run , better  → good , studies → study , went → go
# lemmatization => word ko uski dictionary correct base form mein le aata h.
# This is slow but accurate
""" 
stemming: studies -> studi(just remove word, not check word is correct or not.)
lemmatization: studies -> study(correct dictionary base form)
"""
""" 
Lemma = kisi word ka “dictionary form” (original / base word)
👉 Jo word dictionary mein milta hai
👉 Jiska real meaning hota hai
👉 Jo grammar ke hisaab se correct hota hai
 """

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ['running' , 'better' , 'studies' , 'went']

lemmatized = [lemmatizer.lemmatize(word) for word in words]
print(lemmatized)
# ['running', 'better', 'study', 'went']

print(lemmatizer.lemmatize('better' , pos ='a'))
print(lemmatizer.lemmatize('running' , pos ='v'))
print(lemmatizer.lemmatize('cars' , pos ='n'))
# good
# run
# car
# lemmatization or stemmer ek saath use nhi hote inme se ek hi use hoga code mein

