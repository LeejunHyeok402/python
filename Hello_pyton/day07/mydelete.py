import pymysql

e_id="3"

conn = pymysql.connect(host='localhost',port=3305 ,user='root', password='python',
                       db='python', charset='utf8')
 
curs = conn.cursor()
sql = f"""DELETE FROM emp WHERE e_id='{e_id}';"""

cnt = curs.execute(sql)
print("cnt",cnt)

conn.commit()

curs.close()
conn.close()