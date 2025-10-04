'''
def hailstone(first):
    hails = [first]
    while first > 1:
        if first % 2== 0:
            first = first / 2
        else:
            first = (first * 3) + 1
        hails.append(int(first))
    return hails
first = int(input('enter a number: '))
print(hailstone(first))
'''
def is_acronym(s, list_of_words):
    if len(s)!=len(list_of_words):
        return False
    for i in range(0,len(list_of_words)):
        if list_of_words[i]=='':
            return False
        if s[i]==list_of_words[i][0]:
            return True
        else:
            return False
s='abc'
list_of_words=['apple','banana','coconut']
print(is_acronym(s,list_of_words))











