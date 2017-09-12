from PyQt5 import QtWidgets

from Qtickle import Qtickle
from point_spectra_gui.ui.MaskData import Ui_Form


class Ui_Form(Ui_Form):
    uiID = 0

    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()
        Ui_Form.uiID += 1

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.qt = Qtickle.Qtickle(self)
        self.qt.isGuiChanged(self.qt.guiSave)
        print(Ui_Form.uiID)
        self.pushButton.clicked.connect(lambda: self.on_getDataButton_clicked(self.maskFileLineEdit))

    def on_getDataButton_clicked(self, lineEdit):
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open Mask Data File", '.', "(*.csv)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.csv")

    def getGuiParams(self):
        # TODO put the parameters inside of a list/dictionary
        # TODO create a function that loads in the necessary module
        print(self.qt.guiSave())
        return self.qt.guiSave()