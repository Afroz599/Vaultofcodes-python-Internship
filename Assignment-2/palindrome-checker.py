#user gives string as input
key=input("enter any string\n")
#reversing the string using index values
value=key[::-1]
#comparing both string 
if key==value:
    print("palindrome")
else:
    print("Not a palindrome")
