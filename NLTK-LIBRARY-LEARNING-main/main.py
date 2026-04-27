# nltk stands for natural language tool kit
# use to understand natural language(spoken languages)
# use to train model

# corpora and wordnet
# corpora => corpas se bana h, corpas is large collection of text data
# in machine learning collection of text data is called corpora
# wordnet => A database of English words synonyms, antonyms, meanings.



""" from nltk.corpus import wordnet

syns = wordnet.synsets("Computer")
print(syns[0].definition())
print(syns[0].examples()) """

""" 
sentence = "I love computers"
tokens = sentence.split()
print(tokens)
 """
# Module = file jisme related functions hote hain
# tokenize means split text into word and sentences
# from nltk.tokenize import word_tokenize , sent_tokenize

# text = "I Love my India. This is my India"

# word = word_tokenize(text)
# sent = sent_tokenize(text)
# print(word)
# print(sent)

# from nltk.corpus import stopwords

# stop_words = stopwords.words('english')

# filtered = [w for w in word if w.lower() not in stop_words]

# print(filtered)

""" 
1️⃣ Tokenization => TEXT KO SPLIT KARNA WORD OR SENTENCES MEIN
2️⃣ Stopwords => WORDS_TOKENIZATION MEIN SE COMMAN WORDS(LIKE my, i etc) WORDS KO HATANA
3️⃣ Stemming => WORDS KO UNKI BASE FORM MEIN LEKAR AANA , YE BAS APNA KAAM KARTA HEIN SAHI HO YA GALAT USSE FARK NHI PADTA(EX:- studies = studi(not have any  meaning) , running = run)
4️⃣ Lemmatization
5️⃣ WordNet (LAST)
"""


# practice

""" from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

text = "Childrens are  playing in the deserets and runner , running around forests"
words = word_tokenize(text)
sent = sent_tokenize(text)

print(words)
print(sent)
print()

stop_words = stopwords.words('english')

filtered = [w for w in words if w.lower() not in stop_words]

print("Filtered")
print(filtered)
print()

# plays = play

stemmer = PorterStemmer()

stemmer_words = [stemmer.stem(word) for word in filtered]

print(stemmer_words) """

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = "Children are playing in the desert and roaming around in the forests and studying in the class"

words = word_tokenize(text)
print(f"Words: {words}")
print()

stop_words = stopwords.words('english')
filtered = [w for w in words if w.lower() not in stop_words]
print(f"filtered: {filtered}")
print()

# stemmer = PorterStemmer() # object created // PorterStemmer is the class.

# stem_words = [stemmer.stem(w) for w in filtered]
# print(f"stemmer: {stem_words}")
# print()

# perfomr lemmatization (lemma (dictionary correct base form))

lemmatizer = WordNetLemmatizer() # created object

lemma_words = [lemmatizer.lemmatize(w , pos = 'v') for w in filtered]

print(f"lemma words {lemma_words}")
# lemmatization or stemmer ek saath use nhi hote hai.

""" 
# Bag of Words = text ko numbers (counts) mein badalna
# ex:- I love code and I love nlp.
# I = 2 times , love = 2 , code = 1, and = 1 , nlp = 1 
"""