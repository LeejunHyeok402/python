import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pyqt10.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        self.comList = self.ranCom()
        
    def ranCom(self):
        com = [1,2,3,4,5,6,7,8,9]
        for i in range(100):
            rnd = (int)(random()*9-1)+1;
            a = com[0];
            b = com[rnd];
            com[0] = b;
            com[rnd] = a;
        return com[0:3]
            
    def result(self,com,mine):
        ball = 0
        strike = 0
        for i in range(0,3):
            if com[i] == mine[i]:
                strike += 1
            elif com[i] in mine:
                ball += 1
                
        return strike,ball
    
    def click(self):
        
        print("com:",self.comList)
        
        mine = list(self.le.text())
        mineList = list(map(int,mine))
        print("mine: ", mineList)
        result = self.result(self.comList, mineList)
        
        self.te.append(str(mineList)+": "+str(result[0])+"S, "+str(result[1])+"B")
        
        if result[0] == 3:
            QMessageBox.about(self,'',"정답")
            self.te.setText("")
            self.le.setText("")
            self.comList = self.ranCom()
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()