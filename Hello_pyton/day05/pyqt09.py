import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("pyqt09.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.click)
        self.pb2.clicked.connect(self.click)
        self.pb3.clicked.connect(self.click)
        self.pb4.clicked.connect(self.click)
        self.pb5.clicked.connect(self.click)
        self.pb6.clicked.connect(self.click)
        self.pb7.clicked.connect(self.click)
        self.pb8.clicked.connect(self.click)
        self.pb9.clicked.connect(self.click)
        self.pb0.clicked.connect(self.click)
        self.pb_call.clicked.connect(self.click_call)
    
    def click(self):
        num = self.sender().text()
        old = self.le.text()
        self.le.setText(old+num)
    
    def click_call(self):
        call_num = self.le.text()
        QMessageBox.about(self,'',"calling\n"+call_num)

    
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()