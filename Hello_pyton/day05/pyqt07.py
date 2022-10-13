import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pyqt07.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        
    def click(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        comNum = random()
        if comNum > 0.66:
            com = "가위"
        elif comNum >0.33:
            com = "바위"
        else:
            com = "보"
        
        if com == "가위" and mine == "바위" or com == "바위" and mine =="보" or com =="보" and mine =="가위":
            result = "승리"
        elif com == "가위" and mine == "보" or com == "바위" and mine =="가위" or com =="보" and mine =="바위": 
            result = "패배"
        else:
            result = "비김"
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()