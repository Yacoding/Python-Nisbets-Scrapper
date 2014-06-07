import threading
import time
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import *
import sys
from works.NisbetCat import NisbetCat
from works.NisbetProduct import NisbetProduct

__author__ = 'Rabbi'

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.createGui()

    def createGui(self):
        self.isClickedCategory = False
        self.isClickedProduct = False
        self.browserCat = QTextBrowser()
        self.browserProduct = QTextBrowser()
        self.btnScrapCat = QPushButton('&Start Scraping Category')
        self.btnScrapProduct = QPushButton('&Start Scraping Product')
        layout = QHBoxLayout()

        layoutLeft = QVBoxLayout()
        layoutLeft.addWidget(self.browserCat)
        layoutLeft.addWidget(self.btnScrapCat)

        layoutRight = QVBoxLayout()
        layoutRight.addWidget(self.browserProduct)
        layoutRight.addWidget(self.btnScrapProduct)

        layout.addLayout(layoutLeft)
        layout.addLayout(layoutRight)
        self.setLayout(layout)
        screen = QDesktopWidget().screenGeometry()
        self.resize((screen.width() - 100), (screen.height() - 200))
        self.setWindowTitle("Nisbet Web Scrapper.")
        self.btnScrapCat.clicked.connect(self.btnScrapCatAction)
        self.btnScrapProduct.clicked.connect(self.btnScrapProductAction)

        exit = QAction(self)
        self.connect(exit, SIGNAL('triggered()'), self.closeEvent)

        self.threadCat = None
        self.threadProduct = None

    def btnScrapCatAction(self):
        if self.isClickedCategory is False:
            self.isClickedCategory = True
            self.threadCat = NisbetCat()
            self.threadCat.start()
            self.threadCat.scrapCategoryData.connect(self.addCategoryData)

    def btnScrapProductAction(self):
        if self.isClickedProduct is False:
            self.isClickedProduct = True
            self.threadProduct = NisbetProduct()
            self.threadProduct.start()
            self.threadProduct.scrapProductData.connect(self.addProductData)

    def addCategoryData(self, data):
        self.browserCat.append(str(data))

    def addProductData(self, data):
        self.browserProduct.append(str(data))

    def scrapNisbetProduct(self):
        nisbetProduct = NisbetProduct()
        nisbetProduct.scrapData()

    def closeEvent(self, event):
        if self.threadCat is not None:
            self.threadCat.stop()

        if self.threadProduct is not None:
            self.threadProduct.stop()


class MainView:
    def __init__(self):
        pass

    def showMainView(self):
        app = QApplication(sys.argv)
        form = Form()
        form.show()
        sys.exit(app.exec_())
