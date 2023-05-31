alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def string_encryption(word,key):
    key_list=[]
    answer=''
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word)):
        for b in range (0,len(alphabet)):
            if word[i]==alphabet[b] and step<len(key_list)-1:
                element=b+key_list[step]
                answer+=alphabet[element]
                step+=1
                break
            elif word[i]==alphabet[b] and step==len(key_list)-1:
                element=b+key_list[step]
                answer+=alphabet[element]
                step=0
                break
            elif word[i]==' ':
                answer+=' '
                break
    return answer


def string_decryption(word,key):
    key_list=[]
    answer=''
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word)):
        for b in range (0,len(alphabet)):
            if word[i]==alphabet[b] and step<len(key_list)-1:
                element=b-key_list[step]
                answer+=alphabet[element]
                step+=1
                break
            elif word[i]==alphabet[b] and step==len(key_list)-1:
                element=b-key_list[step]
                answer+=alphabet[element]
                step=0
                break 
            elif word[i]==' ':
                answer+=' '
                break  
    return answer


def list_encryption(word_list,key): 
    key_list=[]
    answer=[]
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word_list)):
        for b in range (0,len(alphabet)):
            if word_list[i]==alphabet[b] and step<len(key_list)-1:
                element=b+key_list[step]
                answer.append(alphabet[element])
                step+=1
                break
            elif word_list[i]==alphabet[b] and step==len(key_list)-1:
                element=b+key_list[step]
                answer.append(alphabet[element])
                step=0
                break 
            elif word_list[i]==' ':
                answer.append(' ')
                break  
    return answer 


def list_decryption(word_list,key):
    key_list=[]
    answer=[]
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word_list)):
        for b in range (0,len(alphabet)):
            if word_list[i]==alphabet[b] and step<len(key_list)-1:
                element=b-key_list[step]
                answer.append(alphabet[element])
                step+=1
                break
            elif word_list[i]==alphabet[b] and step==len(key_list)-1:
                element=b-key_list[step]
                answer.append(alphabet[element])
                step=0
                break 
            elif word_list[i]==' ':
                answer.append(' ')
                break     
    return answer 


def tupple_encryption(word_tupple,key):
    key_list=[] 
    answer=()
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word_tupple)):
        for b in range (0,len(alphabet)):
            if word_tupple[i]==alphabet[b] and step<len(key_list)-1:
                element=b+key_list[step]
                answer+=(alphabet[element],)
                step+=1
                break
            elif word_tupple[i]==alphabet[b] and step==len(key_list)-1:
                element=b+key_list[step]
                answer+=(alphabet[element],)
                step=0
                break 
            elif word_tupple[i]==' ':
                answer+=(' ',)
                break   
    return answer   


def tupple_decryption(word_tupple,key):
    key_list=[] 
    answer=()
    for i in range (0,len(key)):
        for b in range (0,len(alphabet)):
            if key[i]==alphabet[b]:
                key_list.append(b)
                break
    step=0
    for i in range (0,len(word_tupple)):
        for b in range (0,len(alphabet)):
            if word_tupple[i]==alphabet[b] and step<len(key_list)-1:
                element=b-key_list[step]
                answer+=(alphabet[element],)
                step+=1
                break
            elif word_tupple[i]==alphabet[b] and step==len(key_list)-1:
                element=b-key_list[step]
                answer+=(alphabet[element],)
                step=0
                break 
            elif word_tupple[i]==' ':
                answer+=(' ',)
                break   
    return answer   


print('Hello, sir! This is vigenere cipher.\nTell me what you want to do?\n1 - Encryption \t2 - Decryption')
choice=int(input('Answer: '))


if choice==1:
    print('Which one?\n1 - string\t2 - list\t3 - tupple')
    choice=int(input('Answer: '))

    if choice==1:
        word=input('Write a word, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your encrypted message, sir: ',string_encryption(word,key))

    elif choice==2:
        word_list=[]
        print("To end list inputting - input '+' ")
        symbol=input('Write an element, sir: ')
        while symbol!='+':
            word_list.append(symbol)
            symbol=input('Write an element, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your encrypted message, sir: ',list_encryption(word_list,key))

    elif choice==3:
        word_tupple=()
        print("To end tupple inputting - input '+' ")
        symbol=input('Write an element, sir: ')
        while symbol!='+':
            word_tupple+=(symbol,)
            symbol=input('Write an element, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your encrypted message, sir: ',tupple_encryption(word_tupple,key))


elif choice==2:
    print('Which one?\n1 - string\t2 - list\t3 - tupple')
    choice=int(input('Answer: '))

    if choice==1:
        word=input('Write a word, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your decrypted message, sir: ',string_decryption(word,key))

    elif choice==2:
        word_list=[]
        print("To end list inputting - input '+' ")
        symbol=input('Write an element, sir: ')
        while symbol!='+':
            word_list.append(symbol)
            symbol=input('Write an element, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your decrypted message, sir: ',list_decryption(word_list,key))

    elif choice==3:
        word_tupple=()
        print("To end tupple inputting - input '+' ")
        symbol=input('Write an element, sir: ')
        while symbol!='+':
            word_tupple+=(symbol,)
            symbol=input('Write an element, sir: ')
        key=input('Write a key word, sir: ')
        print('here is your encrypted message, sir: ',tupple_decryption(word_tupple,key))
