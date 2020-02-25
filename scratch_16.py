import pypyodbc
conn=pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="C:\Users\AK\Desktop\Database1.accdb";')
cursor1=conn.cursor()
cursor1.execute("SELECT * from students")
rows=cursor1.fetchall()
for i in rows:
    print(i)


