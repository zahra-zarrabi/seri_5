
#translation English to Persian
def my_english():
    user_string=input()
    user_word=user_string.split()
    for n in range(len(user_word)):
        for m in range(len(words)):
            if words[m]['english']==user_word[n]:
                print(words[m]['persian'], end=' ')
                break
        else:
            print(user_word[n],end=' ')

    menu()


#translation Persian to english
def my_persian():
    user_string=input()
    user_word=user_string.split()
    for n in range(len(user_word)):
        for m in range(len(words)):
            if words[m]['persian']==user_word[n]:
                print(words[m]['english'], end=' ')
                break
        else:
            print(user_word[n],end=' ')

    menu()


def new_word():
    user_english=input('Enter english')
    for i in range(len(words)):
        if user_english==words[i]['english']:
            print('This word exists in the word gateway.')
            break
    else:
        user_persian=input('Enter the translation')
        words.append({'english':user_english,'persian':user_persian})
        f=open('translate.txt','a')
        f.write('\n'+user_english+'\n'+user_persian)
        print('Word was added to the word bank.')

    menu()


def menu():
    number=int(input('\n0 translation English to Persian\n1 translation persian to english\n2 add new word\n3 exit\n'))
    if number==0:
        my_english()
    elif number==1:
        my_persian()
    elif number==2:
        new_word()
    elif number==3:
        exit()




try:
    f=open('translate.txt')
except:
    print('Error!')

big_text=f.read()
parts=big_text.split('\n')

words=[]
i=0
while i<len(parts):
    my_Dictionary={'english':parts[i],'persian':parts[i+1]}
    words.append(my_Dictionary)
    i+=2

menu()