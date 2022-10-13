from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from day09.emp_dao import EmpDao

#from emp_dao import EmpDao

app = FastAPI()
ed = EmpDao()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/emp_list", response_class=HTMLResponse)
async def read_item(request: Request):
    
    emps = ed.selects()
    print(emps)
    return templates.TemplateResponse("emp_detail.html", {"request": request,"emps":emps})

#uvicorn myemp:app --reload