#This script will create a users.txt if given a first name and or last name

if __name__ == "__main__" :
    #creatusers.py ascii art
    print("What is the first name?")
    fname = input (">")
    print("What is the last name (optional)")
    lname = input (">")
    if(lname == ""):
        print("meow")
    
    if(lname[0] == " "):
        print("Unexpected space in beginning of last name. Please try again")