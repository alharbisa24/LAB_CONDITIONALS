name= input("write your name: ")
email = input("write your email: ")


if(len(name) > 2 and len(email) > 5 and "@gmail.com" in email):
    print("welcome " + name + " you registered with the email " + email)
elif(len(name) <= 2):
    print("the name length must be more than 2 characters, please provide a valid name.")
elif("@gmail.com" not in email or len(email) <= 5): 
    print("the email is not valid , please provide a valid email.")
