
import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
con.commit()
#cur.execute("create table if not exists students(name varchar(50),email varchar(50),password varchar(50))")
#cur.execute('insert into students values("sweet","sd@12","1234")')
#cur.execute('insert into students values("sol","sd@21","2345")')
#cur.execute('insert into students values("sun jae","sd@13","3456")')
x=cur.execute('select *from students')
print(x.fetchall())
#x=cur.execute("show tables")
con.commit()
print(x)