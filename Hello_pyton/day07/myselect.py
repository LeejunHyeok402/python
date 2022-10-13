import pymysql
 

conn = pymysql.connect(host='localhost',port=3305, user='root', password='python',
                       db='python', charset='utf8')
 

curs = conn.cursor()
 
sql = "select * from emp"
curs.execute(sql)
 
rows = curs.fetchall()
print(rows)

curs.close()
conn.close()

# # Module Imports
# import mariadb
# import sys
# # Connect to MariaDB Platform
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="python",
#         host="localhost",
#         port=3305,
#         database="python"
#     )
#
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)
#
# # Get Cursor
# cur = conn.cursor()
#
# # selectall = "SELECT * from emp" 
# select_all_query = "SELECT * from emp" 
# cur.execute( select_all_query )
#
# # query 결과를 list 형으로 가져옴.
# resultset = cur.fetchall()
#
# for e_id, e_name,sex ,addr in resultset: 
#     print(f"e_id: {e_id} , e_name: {e_name} ,sex: {sex} ,addr: {addr} ")
#
# conn.close ()