import sys
from PySide6 import QtWidgets
import interface


app = QtWidgets.QApplication(sys.argv)

window = interface.MainWindow(app, rtn_data={})

window.show()

app.exec()
