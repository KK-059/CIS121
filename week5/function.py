'''
def reverse_string(word,newword=''):
    for i in range (1,len(word)+1):
        newword=newword+word[-i]
    print (newword)       
word=input('enter a word:')
reverse_string(word)
'''
'''
def fever(giventemp):
    output=False
    unit=giventemp[-1]
    temperature= int(giventemp[:-1])
    if unit=='F' and temperature>98.6:
        output=True
    elif unit=='C' and temperature>37:
        output=True
    else:
        output=False
    return output
giventemp=input('Enter the temperature')
print(f'the temp {giventemp} is fever? {fever(giventemp)}')
'''
'''
def hamming_distance(word1,word2):
    counter=0
    if len(word1)!=len(word2):
        return 0
    
    for i in range (0,len(word1)):
        if word1[i]!=word2[i]:
            counter+=1
    return counter
word1=input('Enter a word')
word2=input('enter another word')
print(f'the hamming distance is {hamming_distance(word1,word2)}')
'''
'''
def last_letters(sentence):
    encode=''
    for i in range(0,len(sentence)):
        if sentence[i]==' ':
            encode=encode+sentence[i-1]
    encode=encode + sentence[-1]
    return encode
sentence=input('enter a sentence:')
print(last_letters(sentence))
'''



