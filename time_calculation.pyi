from typing import Text


calculate_to_sec =24*60*60
calculate_to_minutes =24*60
calculate_to_hours =24
days =int(input("enter the number:"))
if (days<0):
        print("please Enter valied number user")
units =input("Enter the units:")
str(units)
if (units =='seconds'):
    print(days*calculate_to_sec,"sec")    
elif(units =='minutes'):
        print(days*calculate_to_minutes,"min")
elif(units =='hours'):
        print(days*calculate_to_hours,"hours")
else:
    print(SyntaxError)
    

