import re
from collections import defaultdict
import math


#current problems:
#  a chave pode ser maior do que o alfabeto, ou ter letras repetidas ("aa") por exemplo
#  apenas verifica com starting index no 0, e não em outro sítio
#  é possível que a key seja maior do que o que aparece nas opções de decifrar 



def getAllDivisors(num):
    n=[]
    for i in range(1,num+1):
        if (num%i ==0):
            n.append(i)
    return n

def decryption(encrypt_text, key): 
  orig_text = [] 
  for i in range(len(encrypt_text)): 
    x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
    x += ord('a') 
    orig_text.append(chr(x)) 
  return("" . join(orig_text)) 

f = open("1.txt")
s=""
for i in f.readlines():
    s+=i

s=s[0:int(len(s)/5)]


Ngrams = []

for x in range(0, len(s), 3):
    tmpStr = s[x:x+3]
    if (tmpStr not in Ngrams):
        Ngrams.append(tmpStr)


Ngrams = [i for i in Ngrams if len(i) == 3]

indices = {}
for i in Ngrams:
    indices[i] = [ele.start() for ele in re.finditer(i, s)]

for i in Ngrams:
    for x in range(1,len(indices[i])):
        indices[i][x] = indices[i][x] - indices[i][x-1]
    indices[i] = indices[i][1:]
    if(indices[i] == []):
        del indices[i]




#para cada Ngram distance common divisors into dict and count occurrences
divisors = {}
for i in indices:
    for x in indices[i]:
        commons = getAllDivisors(x)
        for z in commons:
            if z not in divisors.keys():
                divisors[z] = 1
            else: 
                divisors[z]+=1


commonlettersPT = ['a','e','o','s','r','i','n','d','m','u','t','c','l','p','v','g','h','q','b','f','z','j','x','k','w','y']
commonlettersENG = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']

divisorsToTest = []
while(len(divisorsToTest)<10):
    tmp = max(divisors, key=divisors.get)
    divisorsToTest.append(tmp)
    del divisors[tmp]

for tmpCommon in [commonlettersENG, commonlettersPT]:
    for size in divisorsToTest:
        Ngrams = []
        for x in range(0, len(s), size):
            tmpStr = s[x:x+size]
            Ngrams.append(tmpStr)
        Ngrams = [i for i in Ngrams if len(i) == size]
        appearances = []
        while(len(appearances)<size):
            appearances.append({})
        for gram in Ngrams:        
            for i in range(0,len(gram)):
                char = gram[i]
                if (char in appearances[i].keys()):
                    appearances[i][char]+=1
                else: 
                    appearances[i][char] = 1
        key = ""
        pos = 0
        for x in appearances:
            mostCommon = max(x, key=x.get)
            toAdd = (ord(mostCommon) - ord(tmpCommon[pos]) + 26) % 26
            toAdd += ord('a') 
            key+= chr(toAdd)
        longkey=""
        print(key)
        while(len(longkey) < len(s)):
            longkey+=key
        print(decryption(s,longkey))

    #[] de dicts do tamanho do N grama atual
    #ir a cada Ngrama e em cada posição vai se acedendo a dicts diferentes
    #para a key vai se buscar as letras mais comuns em cada um e a partir daí são contas


    
"""
key="asd"
longkey = ""
while(len(longkey)<len(s)):
    longkey+="asd"

print(decryption(s,longkey))
"""

# get [common divider]grams and check most common letter in each column

"""
Ngrams = []

for x in range(0, len(s), commonDiv):
    tmpStr = s[x:x+commonDiv]
    Ngrams.append(tmpStr)


Ngrams = [i for i in Ngrams if len(i) == commonDiv]

mostCommonLetters = {}

for gram in Ngrams:
    pos = 0
    for i in gram:
        if (i in mostCommonLetters.keys()):
            while(len(mostCommonLetters[i])< pos+1):
                mostCommonLetters[i].append(0)
            mostCommonLetters[i][pos]+=1
        else: 
            mostCommonLetters[i]=[0]
            while(len(mostCommonLetters[i])< pos+1):
                mostCommonLetters[i].append(0)
            mostCommonLetters[i][pos] = 1
        pos+=1
print(Ngrams)
print(mostCommonLetters)

"""

# first is most, second is second, etc
# math so that those letters are nth common in PT or ENG
# make key on that
# decrypt 
