import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pyqt04.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.click)
        
    def click(self):
        arr45 = [
                1,2,3,4,5       ,6,7,8,9,10,
                11,12,13,14,15  ,16,17,18,19,20,
                21,22,23,24,25  ,26,27,28,29,30,
                31,32,33,34,35  ,36,37,38,39,40,
                41,42,43,44,45 
                ]

        # arr45 = range(1,45+1)
        
        for i in range(100):
            rnd = int(random()*len(arr45))
            a = arr45[0]
            b = arr45[rnd]
            arr45[0]=b
            arr45[rnd]=a
        
        self.le1.setText(str(arr45[0]))
        self.le2.setText(str(arr45[1]))
        self.le3.setText(str(arr45[2]))
        self.le4.setText(str(arr45[3]))
        self.le5.setText(str(arr45[4]))
        self.le6.setText(str(arr45[5]))
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()