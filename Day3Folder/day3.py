# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")

########################################################################
# Task 1:
# name = input("what is your name?")
# title = input("what is your title?")
# task = input("what is the task?")
# print(title, name, "orders the peasants to", task)

########################################################################
# Task 2:



########################################################################
# Task 3:
# num1 = input("what is the first number? ")
# num2 = input("what is the second number? ")
# ans = int(num1) + int(num2)
# print("the answer is", ans)
########################################################################
# Task 4:



########################################################################
# Task 5:
# hidden_password = "passme"
# guess = input("do you know my password")
# if hidden_password == guess:
#     print("please come in")
# else:
#     print("go away or i will call the police")

########################################################################
# Task 6:
# legalage = "21"
# yourage = input("what is your age")
# if legalage <= yourage:
#     print("you are legal to vote for the next president")
# else:
#     print("you are not old enough to vote yet")


########################################################################
# Task 7:



########################################################################
# Task 8:



########################################################################
# Additional exercises:
# Exercise 1

# Write a program to ask the user to enter a password.

# If the password is correct, say "Access Granted"

# Else, say "Access Denied"

# The user is given a change to enter the password 3 times until the correct password is given.
# If the user fails the 3rd attempt, the program will say "System Locked. I call police."



hidden_password = "passme"
tries =3
guess = input("password?")
for count in range(tries):
    if hidden_password == guess:
        print("access granted")
        break
    else:
        print("access denied")
        if count == tries - 1:
            print("System Locked. I call police")


is_correct = False
for count in range(3):
    guess = input("do you know my password")

    if hidden_password == guess:
        print("please come in")
        is_correct = True
        break
    else:print("its okay. try again")

if is_correct == False:
    print("your account is locked")
