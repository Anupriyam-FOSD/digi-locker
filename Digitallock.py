
pwd=float(input("Enter the 4 digit password : "))

if pwd==8969:
    print("Your PC is now unlocked")

else:
    print("Invalid password !!!")
    pwd2=float(input("Press '1' to retry or press '2' to exit : "))
    if pwd2==1:
        pwd=float(input("Enter the 4 digit password : "))
        if pwd==8969:
            print("Your PC is now unlocked")
        else:
            print("Better luck next time :-)")    
    elif pwd2==2:
        print("You failed to login. :(")

    