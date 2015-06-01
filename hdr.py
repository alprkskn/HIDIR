import sys, os
from PyQt4 import QtCore, QtGui, uic, Qt

def supported_image_extensions():
    formats = Qt.QImageReader().supportedImageFormats()
    return [str(fmt) for fmt in formats]

def images(path):
    images = []
    extensions = supported_image_extensions()
    print extensions
    for d in os.listdir(path):
        print d
        if extensions.__contains__(d.split('.')[-1].lower()):
            images.append(d)
    return images

app = QtGui.QApplication(sys.argv)
ui = uic.loadUi('hdr.ui')
ui.show()

lWidget = ui.listWidget
lWidget.clear()
l = QtGui.QListWidget()

ui.fileBrowser.clicked.connect(supported_image_extensions)


for i in images('./hand_held_exposures/bergama_01'):
    item = QtGui.QListWidgetItem(i, None, 1)
    lWidget.addItem(item)

sys.exit(app.exec_())
