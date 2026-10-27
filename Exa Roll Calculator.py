import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
               
        self.ui.genislik.valueChanged.connect(self.calculate)
        self.ui.kalinlik.valueChanged.connect(self.calculate)
        self.ui.uzunluk.valueChanged.connect(self.calculate)
        self.ui.yogunluk.valueChanged.connect(self.calculate)
        self.ui.masura_ag.valueChanged.connect(self.calculate)
        self.ui.koli_ag.valueChanged.connect(self.calculate)
        self.ui.koli_ici_adet.valueChanged.connect(self.calculate)
        
        
        
    def calculate(self):
        
        netfilm_ag = self.ui.genislik.value() * self.ui.kalinlik.value() * self.ui.uzunluk.value() * self.ui.yogunluk.value() / 100000
        brut_rulo_ag = netfilm_ag + (self.ui.masura_ag.value() / 1000)
        brut_koli_ag = (brut_rulo_ag * self.ui.koli_ici_adet.value()) + (self.ui.koli_ag.value() / 1000)
        brut_koli_arti_tol_ag = brut_koli_ag * 1.05
        brut_koli_eksi_tol_ag = brut_koli_ag * 0.95
        
        self.ui.netfilm.setText(str(netfilm_ag))
        self.ui.brut_rulo.setText(str(brut_rulo_ag))
        self.ui.brut_koli.setText(str(brut_koli_ag))
        self.ui.brut_koli_arti_tol.setText(str(brut_koli_arti_tol_ag))
        self.ui.brut_koli_eksi_tol.setText(str(brut_koli_eksi_tol_ag))
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())