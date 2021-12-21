py=float(3.14)
radius= int(input("Enter the radius: "))
Area=float(py*radius*radius)
if radius==0:
    print("Enter the valid number")
elif radius>0:
    print (f"Area of the circle is= {Area} m^2") 
else:
    print("User this is nagtive number please Enter the valid number")