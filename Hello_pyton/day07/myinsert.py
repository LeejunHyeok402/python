import pymysql
 
conn = pymysql.connect(host='localhost',port=3305 ,user='root', password='python',
                       db='python', charset='utf8')
 
curs = conn.cursor()

sql = """INSERT INTO emp(e_id,e_name,sex,addr) VALUES  (%s,%s,%s,%s);"""

cnt = curs.execute(sql, ('3','3', '3','3'))
print("cnt",cnt)
conn.commit()
 
curs.close() 
conn.close()