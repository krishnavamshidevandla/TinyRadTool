from PyQt5 import QtWidgets

class FFT3DWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("3D FFT Window")
        self.resize(600, 400)

    def update_rdm(self):
        pass
