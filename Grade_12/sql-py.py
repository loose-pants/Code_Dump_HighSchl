import sqlite3 as mc
import os
os.chdir('G:\\1Platinum\\Computer practicles')
db=mc.connect('sample')
cur=db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS sqle('no' int(2), 'name' varchar(32),'addr' char(50), 'balance' float,'credlim' float, 'llr' int(2))")
values= ()

qur="insert into sqle values ('1','fjy','rwbbb',210.021,450.042,5.52)"
cur.execute(qur)
qur="insert into sqle values ('1','fjy','rwbbb',210.021,450.20542,85325)"
cur.execute(qur)
cur.execute('select * from sqle')
for i in cur:
    print(i)
db.close()