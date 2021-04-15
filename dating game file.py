def Match_Making_Game():    
    print('Welcome to the Match Making Game!!!!')
    print('Enter the names of the contestants below:')
    name_one = str(input('Name_1:'))
    vowels = 0
    for i in name_one: # this section counts the number of vowels in the name 
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    vowels = vowels + 1
    constants = len(name_one) - vowels #finds number of constants by subracting number of vowels from the amount of characters
    name_one_score = vowels * 5 - constants #finds score of name_one by multiplying number of vowels by 5 then subtracting numer of constants
    print(name_one_score)
    name_two = input('Name_2:') #repeats for name_two
    vowels = 0
    for i in name_two:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    vowels = vowels+1
    constants = len(name_one) - vowels
    name_two_score = vowels * 5 - constants
    print(name_two_score) #compares the scores to find compatiblitly 
    if abs(name_one_score - name_two_score) < 5:
        print('Soulmates')
    elif abs(name_one_score - name_two_score) == 6:
        print('Decent Match')
    elif abs(name_one_score - name_two_score) <= 10:
        print('Decent Match')
    elif abs(name_one_score - name_two_score) >= 11:
        print('May want to try elsewhere')
