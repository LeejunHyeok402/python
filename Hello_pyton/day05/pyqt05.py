import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pyqt05.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.leMine.returnPressed.connect(self.click)
                     
    def click(self):
        a = self.leMine.text()
        com = ""
        result = ""
        b = random()
        if b>0.5:
            com = "짝"
        else:
            com = "홀"
        
        
        if com == a:
            result = "승리"
        else:
            result = "패배" 
            
        self.leCom.setText(com)  
        self.leResult.setText(result)   
        
             
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()