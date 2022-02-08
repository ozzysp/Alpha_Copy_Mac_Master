from PyQt5 import QtWidgets, uic
from src import listdir_function

def selectDevices():
    selected_device = ui_main2.comboBoxFrom.currentText()
    ui_main2.selectDevice.setText('Selected Device -> ' + selected_device)

app = QtWidgets.QApplication([])
ui_main2 = uic.loadUi('ui_main2.ui')
ui_main2.comboBoxFrom.addItems(listdir_function.directories)
ui_main2.scanAgainPB.clicked.connect(selectDevices)


ui_main2.show()
app.exec()
