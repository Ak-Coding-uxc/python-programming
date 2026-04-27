# 17 FEB 2026
# Today topic is Wordnet
""" 
WordNet = English dictionary + relations (computer ke liye)
👉 Ye batata hai:
word ka meaning
same meaning words (synonyms)
opposite meaning (antonyms)
word ka relation dusre words se
* WordNet NLTK ka part hai.

Examples:-
run
Meaning: move fast by foot
Synonyms: sprint, jog
"""

""" 
🔹 IMPORTANT TERM: SYNSET
🔑 Synset = Synonym Set
Synset = same meaning wale words ka group
ex:- {car, auto, automobile}
"""

""" from nltk.corpus import wordnet         

syns = wordnet.synsets('computer')
print(syns)
# [Synset('computer.n.01'), Synset('calculator.n.01')]
Meaning:-
computer → word
n → noun
01 → most common meaning

print(syns[0].name())
print(syns[0].definition())
print(syns[0].examples())
print(syns[0].lemmas()) """

""" WordNet =
✔ dictionary
✔ synonyms ka group
✔ computer-readable format """

""" River bank (kinara)

Bank (money)

👉 Same word, different meanings

WordNet isi confusion ko handle karta hai. """

"""
Bag of Word = WOrd ko number mein badalna . koi word (character nhi) kitni baar repeat hua
ex:- I am. ::==>    I = 1 time ,, am = 1 time
"""

from nltk.corpus import wordnet
syns = wordnet.synsets('umbrella')
print(syns)

# synsets = sets of synonyms
'''
Output :- Synset('bank.n.01')
here bank = word
n = noun
01 = most common meaning
'''

print(syns[0].name())
print(syns[0].definition())
print(syns[0].examples())
print(syns[0].lemmas()) # this return Dictionary correct base form

'''
## syns[0].definition() ka matlab kya hai?
syns → word ke saare meanings
syns[0] → sabse common meaning
.definition() → us meaning ka dictionary meaning
'''


