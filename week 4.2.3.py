n=int(input("Enter no of values"))
dic={}
for i in range(n):
    key=input("Enter key")
    value=input("Enter value")
    dic[key]=value
print(dic)
def invert_content(dic):
    invert_dic={}
    invert_dic={v:k for k,v in dic.items()}
    print("after inversion")
    return invert_dic

print(invert_content)
