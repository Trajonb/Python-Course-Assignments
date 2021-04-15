#trajon brown 
def letters():
    Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Dictionary = {i:0 for i in Alphabet}

    with open('encryptedmac.txt','r+') as f:
        words = f.read()
        
    for i in words:
        for letter in Dictionary:
            if i == letter:
                Dictionary[letter] += 1
    print(Dictionary)
letters()
        
def caesar(text,shift):
    text = text.lower()
    for letter in text:
        if 97 <= ord(letter) <= 122:
            letter = ord(letter)+shift
            if letter > 122:
                new_text = chr(letter-26)
            else:
                new_text = chr(letter)
            print(new_text, end = '')
        else:
            print(letter, end='')
            
def checker(text,shift):
    print()
    caesar(text[:20],shift + 1)
    print('\nDoes this look like english?')
    decision = input('Yes or No: ')
    decision = decision.upper()
    while decision != 'Yes':
        shift += 1
        print()
        caesar(text[:20], shift)
        print()
        decision = input('How about now\n Yes or No: ')
    
    print('Here is the whole decoded file')
    caesar(text,shift)
    
def decode():
    try:
        file_name = input('Enter File name: ')
        with open(file_name, 'r+') as f:
            text = f.read()
    except:
        print('Could not find the file!')
        #print(text)      
    checker(text,1)
    shift = 0
    caesar(text[:20],shift + 1)
    print('\nDoes this look like english?')
    decision = input('Yes or No: ')
    decision = decision.upper()
    while decision != 'Yes':
        shift += 1
        print()
        caesar(text[:20], shift)
        print()
        decision = input('How about now\n Yes or No: ')
    print('Here is the whole decoded file')
    caesar(text,shift)

        
    
          
    

    
        
