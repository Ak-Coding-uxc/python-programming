# regular expression
""" 
koi cheez kaha kaha h iss liye bhi use hota h.

-- Regex (Regular Expression) Kya Hai?
Simple definition:
Regex ek pattern hai jo text में kuch dhoondhne ke liye use hota hai.


 """
import re

pattern = r"[A-Z]+aptiste"
# r = row string, means \n joh h wo exactly print hoga new line nhi aayegi , escape sequence character ko parse nhi karega
text = '''
The Young Head coinage consists of the issues of British coins with an obverse bust of Queen Victoria first used in 1838 
while she was still a teenager. The bust was designed by William Wyon and remained on Paptiste some British coins until 1887,
by which time she was almost 70 years of age and had ceased to resemble her depiction. The young Kaptiste queen sat for Wyon in 
August and September 1837. Wyon then created his coinage portrait of her, which was approved in February 1838, and production began
later that year. Some of the new coins had reverses by Wyon, others by Jean Zaptiste Merlen.
'''

# match = re.search(pattern,text)
# print(match)

matches = re.finditer(pattern,text)

for match in matches:
    print(type(match.span()))

