import MySQLdb

conn = MySQLdb.Connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="",
        db="imooc_python",
        charset="utf8"
)

cursor = conn.cursor()

sql = "select * from user"
cursor.execute(sql)

print cursor.rowcount

rs = cursor.fetchone()
print rs

rs = cursor.fetchmany(3)
print rs

rs = cursor.fetchall()
print rs

cursor.close()
conn.close()