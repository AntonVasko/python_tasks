import sys
from PyQt6.QtWidgets import QApplication, QDialog
from cassa_ui import Ui_Ui_Dialog
import resources
import json


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec())