import sqlite3 as sq
import logging as lg


dname = 'sample.db'
conn = sq.connect(dname)
lg.basicConfig(filename='example.log')

ex_data = ["id ","name "]
i_data = [[0,'master',]]
com = ['0','master']
cnt = 0
while com[0] != 'end':
    print(com)
    print(i_data)
    i_data.append(com)
    for i in range(2):
        print(ex_data[i],end="")
        com[i] = input(": ")
        if com[i] == 'end':
            cnt -= 1
            break
        else:
            com[0] = int(com[0])
            cnt+=1
    
print(cnt)
for i in range(cnt):
    for j in range(2):
        print(i,j)
        print("insert into sample(",ex_data[j],")values(",i_data[i][j],")")

print(i_data)
"""
cur = conn.cursor()

cur.execute('insert into sample(name)values("Taro")')
cur.execute('insert into sample(name)values("Hanako")')

cur.execute("select * from sample")

data = cur.fetchall()
for i in data:
    print(i)

conn.commit()
cur.close()

conn.close()
"""
