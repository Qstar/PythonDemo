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

print conn
print cursor

cursor.close()
conn.close()
