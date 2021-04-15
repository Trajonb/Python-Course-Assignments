'''Trajon Brown
11/7/18
Inspirational Text project
'''
#Starter code from https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
#Info on ports here: https://support.desk.com/customer/portal/articles/1741-configuring-smtp-servers-to-send-email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def sendEmail():
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(sender, password)
    msg = MIMEMultipart()
    msg['From']= sender
    msg['To']= sendee
    msg['Subject']= header
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    del msg
    s.quit()
    
def menu(): #menu of options
    print('1. Count Occurences\n2. Find Occurence\n3. Search and Replace\n4. Encode the Text\n5. Read Backwards\n6. Email a random chunk of text with key word\n7. Email a random chunk of text\n8. Quit')            
print('Hello, Let me inpire you!')
try_loop = True
while try_loop == True:
    try:
        file_name = input('Enter File name: ')
        with open(file_name, 'r+') as f:
            text = f.read()
            try_loop = False
    except:
        print('Could not find the file!')
       
menu()
main_menu = 'M'
import random 
while main_menu == 'M' or main_menu == 'm' : # keeps looping menu when they press m
    number_input = input('Enter a number: ')
    if number_input == '1': #word occurence
        print('What word or Phrase would you like to search? ')
        word = str(input())
        print(word + ' occurs ' + str(text.count(word)) + ' time!')
        main_menu = input('Enter M to show menu!: ')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':
            print('Okay, Bye!')
    elif number_input == '2': #find word
        print('What word would you like my to find?')
        word = str(input())
        new = text.split()
        position = new.index(word)
        print(' '.join(new[position-10:position] + new[position: position + 10]))
        
        
        main_menu = input('Enter M to show menu!: ')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':
            print('Okay, Bye!')
    elif number_input == '3': #search and replace
        text = text.lower()
        new_text = text.split()
        print('What word would you like me to replace?')
        word = str(input())
        print('What word would you like to replace with?')
        replace_word = str(input())
        replaced_text = text.replace(word, replace_word)
        print(replaced_text, '\nOkay, it has been replaced')
        main_menu = input('Enter M to show menu!: ')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':
            print('Okay, Bye!')
    elif number_input == '4': #encode text 
        shift = input('Enter the amount of shifts: ')
        print('The text will be saved as a different text file name New_file.txt')
        shift = int(shift)
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
            with open('New_file.txt', 'w+') as f:
                 f.write(new_text)
        main_menu = input('Enter M to show menu!: ')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':
            print('Okay, Bye!')
    elif number_input == '5': #read backwards
        print(text[::-1])
        main_menu = input('Enter M to show menu!: ')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':
            print('Okay, Bye!')
    elif number_input == '6': # send email
        sender = 'tdogbreezy2323@gmail.com'
        sendee = input('What is your email?')
        header = 'Inspirational Email'
        key_word = str(input('Enter keyword: '))
        new = text.split()
        position = new.index(key_word)
        body = ' '.join(new[position-10:position] + new[position: position + 10])
        password = 'Tdogbreezy232729'              
        sendEmail()
        print('You have received a email!')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M': # Quit program 
            print('Okay, Bye!')
    elif number_input == '7': # send email
        sender = 'tdogbreezy2323@gmail.com'
        sendee = input('What is your email?')
        header = 'Inspirational Email'
        new = text.split()
        position = random.randint(1,100)
        body = ' '.join(new[position-10:position] + new[position: position + 10])
        password = 'Tdogbreezy232729'              
        sendEmail()
        print('You have received a email!')
        if main_menu == 'M' or main_menu == 'm':
            menu()
        elif main_menu != 'M':  
            print('Okay, Bye!')        
    elif number_input == '8': # Quitting program
        print('okay, See yah!')
        break
        
 
        
 
                
            

        
        
    
    
