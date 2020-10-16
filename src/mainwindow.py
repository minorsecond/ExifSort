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
            "Camera Manufacturer": '0x010f',
            "Camera Model": '0x0110',
            "Camera Orientation": '0x0112',
            "Image X Resolution": '0x011a',
            "Image Y Resolution": '0x011b',
            "Exposure Time": '0x829a',
            "FD Number": '0x829d',
            "ISO": '0x8827',
            "Date & Time Created": '0x9003',
            "Aperture Value": '0x9202',
            "Brightness Value": '0x9203',
            "Exposure Compensation": '0x9204',
            "Metering Mode": '0x9207',
            "Image Number": '0x9211',
            "Exposure Mode": '0xa402',
            "White Balance Mode": '0xa403',
            "Camera Serial Number": '0xa431',
            "Lens Make": '0xa433',
            "Lens Model": '0xa434',
            "Lens Serial Number": '0xa435',
        }

        self.exif_attributes = {key: value for key, value in sorted(self.exif_attributes.items())}

        print(self.exif_attributes)

        for attribute in self.exif_attributes:
            self.attributeSelectorInput.addItem(attribute)
