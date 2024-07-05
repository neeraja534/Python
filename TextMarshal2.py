import marshal
fp=open("marshal2.txt","rb")
data=marshal.load(fp)
exec(data)
fp.close()