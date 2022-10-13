from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel
import pymysql

app = FastAPI()

def my_select():
    conn = pymysql.connect(host='localhost',port=3305, user='root', password='python',
                       db='python', charset='utf8')
 
    curs = conn.cursor()
     
    sql = "select * from emp"
    curs.execute(sql)
     
    rows = curs.fetchall()
    print(rows)
    
    curs.close()
    conn.close()
    
    return rows

@app.get("/")
async def root():
    return "hello worel"
@app.get("/select")
async def select():
    result = my_select()
    return result

@app.get("/hello", response_class=HTMLResponse)
async def hello():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """

@app.get("/dan", response_class=HTMLResponse)
async def dan(dan:Optional[str]="9"):
    idan = int(dan)
    html = ""
    for i in range(1,9+1):
        html += f"{idan}*{i}={idan*i}<br>"
    
    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {html}
        </body>
    </html>
    """

@app.post("/dan", response_class=HTMLResponse)
async def dan_post(dan: str = Form()):
    idan = int(dan)
    html = ""
    for i in range(1,9+1):
        html += f"{idan}*{i}={idan*i}<br>"
    
    return f"""
    <html>
        <head>
            <title>구구단</title>
        </head>
        <body>
            {html}
        </body>
    </html>
    """
    
