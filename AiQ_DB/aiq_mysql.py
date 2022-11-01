import mysql.connector
from mysql.connector import Error

host = '220.128.122.69' #連接資料庫IP位址
db = 'rtls'             #連接資料表名稱
user = 'root'           #使用者ID
password = 'King1234'   #使用者密碼


def sql_get():
    conn = mysql.connector.connect(
        host = host,
        database = db,
        user = user,
        password = password)#設定連接資料庫所有參數

    cur = conn.cursor() #連接資料庫
    # cur.execute("SELECT * FROM rtls.tag WHERE Id = 'D8FE8BEFD79E';")
    cur.execute("SELECT * FROM tag")    #執行所要的SQL語言
    record = cur.fetchall() #將返回所有接收到的資料
    return (record)

