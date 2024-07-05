ch=input("Enter the character")
if(ch.islower()):
    print(ch,"is lower case alphabet")
elif(ch.isupper()):
    print(ch,"is Upper case alphabet")
elif(ord(ch)>=48 and ord(ch)<=57):
    print(ch,"is digit")
else:
    print(ch,"is special character")