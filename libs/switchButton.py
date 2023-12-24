# coding: utf-8
from PyQt5.QtCore import QFile, Qt, QTimer, pyqtProperty, pyqtSignal
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QToolButton, QWidget
BUTTONQSS="""QWidget{
    background-color: transparent;
}

SwitchButton {
    qproperty-spacing: 15;
}

SwitchButton > QLabel {
    color: black;
    font-family: "微软雅黑";
    font-size:14px;
}


Indicator {
    height: 12px;
    width: 35px;
    qproperty-sliderOnColor: white;
    qproperty-sliderOffColor: black;
    qproperty-sliderDisabledColor: rgb(155, 154, 153);
    border-radius: 11px;
}


Indicator:!checked {
    background-color: transparent;
    border: 1px solid rgb(102, 102, 102);
}

Indicator:!checked:hover {
    border: 1px solid rgb(51, 51, 51);
    background-color: transparent;
}

Indicator:!checked:pressed {
    border: 1px solid rgb(0, 0, 0);
    background-color: rgb(153, 153, 153);
}

Indicator:checked {
    border: 1px solid rgb(0, 153, 188);
    background-color: rgb(0, 153, 188);
}

Indicator:checked:hover {
    border: 1px solid rgb(72, 210, 242);
    background-color: rgb(72, 210, 242);
}

Indicator:checked:pressed {
    border: 1px solid rgb(0, 107, 131);
    background-color: rgb(0, 107, 131);
}

Indicator:disabled:!checked{
    border: 1px solid rgb(194, 194, 191);
    background-color: rgb(230,230,230);
}
Indicator:disabled:checked{
    border: 1px solid rgb(194, 194, 191);
    background-color: rgb(135, 172, 182);
    qproperty-sliderDisabledColor: rgb(221, 221, 221);
}"""

class Indicator(QToolButton):
    """ Indicator of switch button """

    checkedChanged = pyqtSignal(bool)

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setCheckable(True)
        super().setChecked(False)
        self.resize(50, 26)
        self.__sliderOnColor = QColor(Qt.white)
        self.__sliderOffColor = QColor(Qt.black)
        self.__sliderDisabledColor = QColor(QColor(155, 154, 153))
        self.timer = QTimer(self)
        self.padding = self.height()//4
        self.sliderX = self.padding
        self.sliderRadius = (self.height()-2*self.padding)//2
        self.sliderEndX = self.width()-2*self.sliderRadius
        self.sliderStep = self.width()/50
        self.timer.timeout.connect(self.__updateSliderPos)
    def __updateSliderPos(self):
        """ update slider position """
        if self.isChecked():
            if self.sliderX+self.sliderStep < self.sliderEndX:
                self.sliderX += self.sliderStep
            else:
                self.sliderX = self.sliderEndX
                self.timer.stop()
        else:
            if self.sliderX-self.sliderStep > self.sliderEndX:
                self.sliderX -= self.sliderStep
            else:
                self.sliderX = self.sliderEndX
                self.timer.stop()

        self.style().polish(self)
    def setChecked(self, isChecked: bool):
        """ set checked state """
        if isChecked == self.isChecked():
            return

        super().setChecked(isChecked)
        #-2*self.sliderRadius错误，已改正
        self.sliderEndX = self.width() - \
            self.padding if self.isChecked() else self.padding
        self.timer.start(5)

    def mouseReleaseEvent(self, e):
        """ toggle checked state when mouse release"""
        super().mouseReleaseEvent(e)
        self.sliderEndX = self.width()-2*self.sliderRadius - \
            self.padding if self.isChecked() else self.padding
        self.timer.start(5)
        self.checkedChanged.emit(self.isChecked())

    def resizeEvent(self, e):
        self.padding = self.height()//4
        self.sliderRadius = (self.height()-2*self.padding)//2
        self.sliderStep = self.width()/50
        self.sliderEndX = self.width()-2*self.sliderRadius - \
            self.padding if self.isChecked() else self.padding
        self.update()

    def paintEvent(self, e):
        """ paint indicator """
        # the background and border are specified by qss
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        if self.isEnabled():
            color = self.sliderOnColor if self.isChecked() else self.sliderOffColor
        else:
            color = self.sliderDisabledColor
        painter.setBrush(color)
        painter.drawEllipse(self.sliderX, self.padding,
                            self.sliderRadius*2, self.sliderRadius*2)

    def getSliderOnColor(self):
        return self.__sliderOnColor

    def setSliderOnColor(self, color: QColor):
        self.__sliderOnColor = color
        self.update()

    def getSliderOffColor(self):
        return self.__sliderOffColor

    def setSliderOffColor(self, color: QColor):
        self.__sliderOffColor = color
        self.update()

    def getSliderDisabledColor(self):
        return self.__sliderDisabledColor

    def setSliderDisabledColor(self, color: QColor):
        self.__sliderDisabledColor = color
        self.update()

    sliderOnColor = pyqtProperty(QColor, getSliderOnColor, setSliderOnColor)
    sliderOffColor = pyqtProperty(QColor, getSliderOffColor, setSliderOffColor)
    sliderDisabledColor = pyqtProperty(
        QColor, getSliderDisabledColor, setSliderDisabledColor)


class SwitchButton(QWidget):
    """ Switch button class """

    clicked = pyqtSignal(bool)

    def __init__(self,parent):
        super().__init__(parent=parent)
        self.text = ""
        self.__spacing = 15
        self.hBox = QHBoxLayout(self)
        self.indicator = Indicator(self)
        self.label = QLabel(self.text, self)
        self.__initWidget()

    def __initWidget(self):
        """ initialize widgets """
        # set layout
        self.hBox.addWidget(self.indicator)
        self.hBox.addWidget(self.label)
        self.hBox.setSpacing(self.__spacing)
        self.hBox.setAlignment(Qt.AlignLeft)
        self.setAttribute(Qt.WA_StyledBackground)
        self.hBox.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(BUTTONQSS)

        # connect signal to slot
        self.indicator.checkedChanged.connect(self.clicked)
    def isChecked(self):
        return self.indicator.isChecked()

    def setChecked(self, isChecked: bool):
        """ set checked state """
        # self.adjustSize()
        self.indicator.setChecked(isChecked)

    def toggleChecked(self):
        """ toggle checked state """
        self.indicator.setChecked(not self.indicator.isChecked())

    def setText(self, text: str):
        self.text = text
        self.label.setText(text)
        self.adjustSize()

    def getSpacing(self):
        return self.__spacing

    def setSpacing(self, spacing: int):
        self.__spacing = spacing
        self.hBox.setSpacing(spacing)
        self.update()

    spacing = pyqtProperty(int, getSpacing, setSpacing)