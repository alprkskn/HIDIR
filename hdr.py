import sys, os
from PyQt4 import QtCore, QtGui, uic, Qt

dirpath = '.'

def supported_image_extensions():
    formats = Qt.QImageReader().supportedImageFormats()
    return [str(fmt) for fmt in formats]

def images(path):
    images = []
    extensions = supported_image_extensions()
    for d in os.listdir(path):
        print d
        if extensions.__contains__(d.split('.')[-1].lower()):
            images.append(d)
    images.sort() #TODO: Sort by exposure levels
    return images

def populate_list(widget, lst):
    widget.clear()
    for i in lst:
        item = QtGui.QListWidgetItem(i, None, 0)
        print str(dirpath) + '/' + str(i)
        item.setIcon(Qt.QIcon(str(dirpath) + '/' + str(i)))
        widget.addItem(item)

def set_dirpath(widget, path):
    global dirpath
    dirpath = path
    l = images(path)
    populate_list(widget, l)

app = QtGui.QApplication(sys.argv)
ui = uic.loadUi('hdr.ui')
ui.show()

lWidget = ui.listWidget
ui.fileBrowser.clicked.connect(supported_image_extensions)

set_dirpath(lWidget, './hand_held_exposures/hk_temple_16')


sys.exit(app.exec_())
