#Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.

n1=int(input("enter 1st number\n"))
n2=int(input("enter 2nd number\n"))
n3=int(input("enter 3rd number\n"))
if n1>n2 and n1>n3:
    print(n1,"is greater among three")
elif n1>n2 and n1<n3:
    print(n3,"is greater among three")
else:
    print(n2,"is greater among three")       