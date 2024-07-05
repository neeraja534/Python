import marshal
src='''
n=10
if n==1 or n==0:
        return 1
else:
  return n*factorial(n-1)
'''
code=compile(src,"src","exec")
fp=open("marshal2.txt","wb")
marshal.dump(code,fp)
fp.close()