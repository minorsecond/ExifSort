from gui import ui_mainwindow
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    """
    Main UI Class
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui_mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(632, 300)

        self.exif_attributes = {
            "Camera make {cmake}": '0x010f',
            "Camera Model {cmodel}": '0x0110',
            "Camera Orientation {corient}": '0x0112',
            "Image X Resolution {xres}": '0x011a',
            "Image Y Resolution {yres}": '0x011b',
            "Exposure Time {etime}": '0x829a',
            "FD Number {fdnum}": '0x829d',
            "ISO {iso}": '0x8827',
            "Date & Time Created {dtime}": '0x9003',
            "Aperture Value {aperval}": '0x9202',
            "Brightness Value {bright}": '0x9203',
            "Exposure Compensation {excomp}": '0x9204',
            "Metering Mode {meter}": '0x9207',
            "Image Number {inum}": '0x9211',
            "Exposure Mode {exmode}": '0xa402',
            "White Balance Mode {wb}": '0xa403',
            "Camera Serial Number {cserial}": '0xa431',
            "Lens Make {lmake}": '0xa433',
            "Lens Model {lmodel}": '0xa434',
            "Lens Serial Number {lserial}": '0xa435',
        }

        self.exif_attributes = {key: value for key, value in sorted(self.exif_attributes.items())}

        for attribute in self.exif_attributes:
            self.attributeSelectorInput.addItem(attribute)
