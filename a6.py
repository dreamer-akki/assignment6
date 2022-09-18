#Write a python script to check whether a given number is a three digit number or not.

num=int(input("Enter the number\n"))
if num>99 and num<1000:
    print("It is a three digit number")
else:
    print("it is not a three digit number")    