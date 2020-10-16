from gui import ui_mainwindow
from src import image_read
from PyQt5 import QtWidgets
import os
import re


class MainWindow(QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    """
    Main UI Class
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui_mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(632, 300)
        self.progressBar.setValue(0)

        # Set connections
        self.mainButtonBox.accepted.connect(self.read_images)
        self.populate_attribute_picker()

    def populate_attribute_picker(self):
        """
        Populate the attribute picker with valid values.
        """

        self.exif_attributes = {
            "Camera make {cmake}": 'Exif.Image.Make',
            "Camera Model {cmodel}": 'Exif.Image.Model',
            "Camera Orientation {corient}": 'Exif.Image.Orientation',
            "Image X Resolution {xres}": 'Exif.Photo.FocalPlaneXResolution',
            "Image Y Resolution {yres}": 'Exif.Photo.FocalPlaneYResolution',
            "Exposure Time {etime}": 'Exif.Photo.ExposureTime',
            "FD Number {fdnum}": 'Exif.Photo.FNumber',
            "ISO {iso}": 'Exif.Photo.ISOSpeedRatings',
            "Date & Time Created {dtime}": 'Exif.Photo.DateTimeOriginal',
            "Aperture Value {aperval}": 'Exif.Photo.ApertureValue',
            "Metering Mode {meter}": 'Exif.Photo.MeteringMode',
            "Image Number {inum}": 'Exif.Image.ImageNumber',
            "Exposure Mode {exmode}": 'Exif.Photo.ExposureMode',
            "White Balance Mode {wb}": 'Exif.Photo.WhiteBalance',
            "Camera Serial Number {cserial}": 'Exif.Photo.BodySerialNumber',
            "Lens Make {lmake}": 'Exif.Photo.LensMake',
            "Lens Model {lmodel}": 'Exif.Photo.LensModel',
            "Lens Serial Number {lserial}": 'Exif.Photo.LensSerialNumber',
        }

        self.exif_attributes = {key: value for key, value in sorted(self.exif_attributes.items())}

        for attribute in self.exif_attributes:
            self.attributeSelectorInput.addItem(attribute)

    def get_attributes(self):
        """
        Get the attributes from the text input bar
        :return: Selected attributes that correspond to dictionary keys from Py3Exiv2
        """

        filename_structure = self.filenameFormatLineEdit.text()
        pattern = "{(.*?)}"
        selected_attributes = re.findall(pattern, filename_structure)
        attributes_to_get = []

        for name, exif_tag in self.exif_attributes.items():
            tag_abbrev = re.findall(pattern, name)[0]
            if tag_abbrev in selected_attributes:
                attributes_to_get.append(exif_tag)

        return attributes_to_get

    def read_images(self):
        """
        Read the images found within path
        :return: a list of Image objects
        """

        file_extensions = []
        images = []
        input_path = self.inputPathEdit.text()

        attributes_to_get = self.get_attributes()

        if self.jpgCheckBox.isChecked():
            file_extensions.extend([".jpg", ".jpeg"])
        if self.rawCheckBox.isChecked():
            file_extensions.extend([".raw", ".cr2", ".dng"])
        if self.tiffCheckBox.isChecked():
            file_extensions.extend([".tiff", ".tif"])

        for root, dirnames, filenames in os.walk(input_path):
            for file in filenames:
                if os.path.splitext(file)[1].lower() in file_extensions:
                    source_path = os.path.join(root, file)
                    image = image_read.Image(source_path)
                    images.append(image)
