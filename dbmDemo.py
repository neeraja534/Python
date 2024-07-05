import dbm
db=dbm.open("dbml.db","n")
db['one']='1'
db['two']='2'
db['three']='3'
#with dbm.open("dbml.db")as db: