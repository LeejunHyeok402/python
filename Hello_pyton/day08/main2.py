from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pymysql

app = FastAPI()


def my_select():
    conn = pymysql.connect(host='localhost',port=3305, user='root', password='python',
                       db='python', charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
 #cursorclass=pymysql.cursors.DictCursor 이걸 넣으면 키값도 같이 가져옴
    curs = conn.cursor()
     
    sql = "select e_id,e_name,sex,addr from emp"
    curs.execute(sql)
     
    rows = curs.fetchall()
    print(rows)
    
    curs.close()
    conn.close()
    
    return rows

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    str = "패스트 api 겁나 짜증남"
    arr = ["홍길동","전우치","이순신"]
    emps = [
        {'e_id':'1','e_name':'1','sex':'1','addr':'1'},
        {'e_id':'2','e_name':'2','sex':'2','addr':'2'},
        {'e_id':'3','e_name':'3','sex':'3','addr':'3'}
        ]
    emps_indb = my_select()
    return templates.TemplateResponse("index.html", {"request": request,"str":str,"arr":arr,"emps":emps,"emps_indb":emps_indb})

#uvicorn main2:app --reload