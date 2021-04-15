#Trajon Brown
with open("Bucketlist.txt","w") as f: #writes the list in a file
          f.write("Do a backlflip\n" "Go to Paris\n" "Sing on stage\n" "Make a million dollars\n" "Skydive\n" "Learn guitar\n")
with open("Bucketlist.txt","a") as f: #adds a new item to list 
          f.write("Become a master at Python\n")        
with open("Bucketlist.txt","r") as f:
    string = f.read()
    new_string = string.replace("Python","a new language")
with open("Bucketlist.txt","w")as f:
    f.write(new_string)
