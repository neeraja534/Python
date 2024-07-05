import dbm
db=dbm.open("dbml","r")
print(list(dbm.keys()))
print(list(dbm.valus()))
