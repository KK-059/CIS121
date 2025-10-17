#debugger shit basically learning how to debug and stuff
def strin_to_list_with_vowels(word):
    words=[]
    counter=0
    #collect a w
    built_word=''
    new_word=[]
    vowel_count=0
    for letter in word:
        if letter == ' ':
            words.append(built_word)
            built_word=''
        else:
            built_word=built_word+letter
    for things in words:
        for vowels in things:
            if vowels in 'aeiou':
                counter=counter+1
        if counter>=2:
            new_word.append(things)
            counter=0
    return new_word
my_word='peter piper picked a peck of pickled pepper'
print(strin_to_list_with_vowels(my_word))