#Write a python script to take the month value in numeric format and display the number of days in it.

mon=int(input("enter the month in numeric format\n"))
if mon==1:
    print("January has 31 days")
elif mon==2:
    print("Febuary has 28 or 29 days") 
elif mon==3:
    print("March has 31 days") 
elif mon==4:
    print("April has 30 days") 
elif mon==5:
    print("May has 31 days") 
elif mon==6:
    print("June has 30 days") 
elif mon==7:
    print("July has 31 days") 
elif mon==8:
    print("August has 31 days")     
elif mon==9:
    print("September has 30 days")   
elif mon==10:
    print("October has 31 days") 
elif mon==11:
    print("November has 30 days")                                        
elif mon==12:
    print("December has 31 days")   
else:
    print("Enter a valid month")    