from gui import ui_mainwindow
from src import image_read
from PyQt5 import QtWidgets
import math
import os
import re
import shutil


class MainWindow(QtWidgets.QMainWindow, ui_mainwindow.Ui_MainWindow):
    """
    Main UI Class
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        ui_mainwindow.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(632, 325)
        self.progressBar.setValue(0)
        self.outputPathEdit.setDisabled(True)
        self.outputPathBrowseButton.setDisabled(True)

        # Whitespace replacement options
        for replacement_char in ("None", '.', '_', '-'):
            self.whiteSpaceReplacementSelector.addItem(replacement_char)

        # Set connections
        self.mainButtonBox.accepted.connect(self.process_images)
        self.attributeSelectorInput.activated.connect(self.add_attribute)
        self.seperateOutputPathCheckbox.stateChanged.connect(self.enable_disable_output_path_edit)
        self.inputPathBrowseButton.clicked.connect(self.get_input_directory)
        self.outputPathBrowseButton.clicked.connect(self.get_output_directory)

        self.exif_attributes = {
            "Camera Make {cmake}": 'Exif.Image.Make',
            "Camera Model {cmodel}": 'Exif.Image.Model',
            "Camera Orientation {corient}": 'Exif.Image.Orientation',
            "Image X Resolution {xres}": 'Exif.Photo.FocalPlaneXResolution',
            "Image Y Resolution {yres}": 'Exif.Photo.FocalPlaneYResolution',
            "Exposure Time {etime}": 'Exif.Photo.ExposureTime',
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

        self.populate_attribute_picker()

    def get_input_directory(self):
        """
        Gets the input directory.
        :return: Input path.
        """

        input_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Input Directory"))
        self.inputPathEdit.setText(input_path)

    def get_output_directory(self):
        """
        Gets the output directory.
        :return: Output path.
        """

        output_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Output Directory"))
        self.outputPathEdit.setText(output_path)

    def populate_attribute_picker(self):
        """
        Populate the attribute picker with valid values.
        """

        self.exif_attributes = {key: value for key, value in sorted(self.exif_attributes.items())}

        for attribute in self.exif_attributes:
            self.attributeSelectorInput.addItem(attribute)

    def get_attributes(self):
        """
        Get the attributes from the text input bar
        :return: Selected attributes that correspond to dictionary keys from Py3Exiv2
        """

        filename_structure = self.pathFormatLineEdit.text()
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

        if self.jpgCheckBox.isChecked():
            file_extensions.extend([".jpg", ".jpeg"])
        if self.rawCheckBox.isChecked():
            file_extensions.extend([".raw", ".cr2", ".dng"])
        if self.tiffCheckBox.isChecked():
            file_extensions.extend([".tiff", ".tif"])

        for root, directory_names, filenames in os.walk(input_path):
            for file in filenames:
                if os.path.splitext(file)[1].lower() in file_extensions:
                    source_path = os.path.join(root, file)
                    image = image_read.Image(source_path)
                    images.append(image)
        return images

    def add_attribute(self):
        """
        Add attribute to filename format bar when clicked in picker.
        """

        chosen_attribute = self.attributeSelectorInput.currentText()
        pattern = "{(.*?)}"
        chosen_attribute = re.search(pattern, chosen_attribute).group()
        filename_format_text = self.pathFormatLineEdit.text()
        filename_format_text += chosen_attribute
        self.pathFormatLineEdit.setText(filename_format_text)

    def replace_whitespaces(self, string):
        """
        Replaces whitespaces in string with selected character.
        :param string: String denoting path that should have whitespaces removed.
        :return: Path with whitespaces removed.
        """

        if self.whiteSpaceReplacementSelector.currentText() == '.':
            return string.replace(' ', '.')
        elif self.whiteSpaceReplacementSelector.currentText() == '_':
            return string.replace(' ', '_')
        elif self.whiteSpaceReplacementSelector.currentText() == '-':
            return string.replace(' ', '-')
        else:
            return string

    def format_to_path(self, images, output_path):
        """
        Move the images
        """

        images_with_paths = {}
        # Replace all substrings with EXIF attributes
        for image in images:
            image_filename = os.path.basename(image.source_path)

            # Format values
            aperture_value = str(round(math.pow(2, float(image.aperture_value / 2)), 1))

            path_format = self.pathFormatLineEdit.text()
            path_format = path_format.replace("{cmake}", image.camera_make)
            path_format = path_format.replace("{cmodel}", image.camera_model)
            path_format = path_format.replace("{cserial}", image.camera_serial_num)
            path_format = path_format.replace("{corient}", str(image.camera_orientation))
            path_format = path_format.replace("{xres}", str(image.x_resolution))
            path_format = path_format.replace("{yres}", str(image.y_resolution))
            path_format = path_format.replace("{etime}", str(image.exposure_time))
            path_format = path_format.replace("{iso}", str(image.iso))
            path_format = path_format.replace("{dtime}", image.datetime)
            path_format = path_format.replace("{aperval}", aperture_value)
            path_format = path_format.replace("{meter}", str(image.meter_mode))
            path_format = path_format.replace("{inum}", str(image.image_number))
            path_format = path_format.replace("{xmode}", str(image.exposure_mode))
            path_format = path_format.replace("{wb}", str(image.white_balance))
            path_format = path_format.replace("{lmake}", image.lens_make)
            path_format = path_format.replace("{lmodel}", image.lens_model)
            path_format = path_format.replace("{lserial}", image.lens_serial_num)

            # Build the dict
            path_format = self.replace_whitespaces(path_format)
            new_root_path = os.path.join(output_path, path_format)
            new_image_path = os.path.join(new_root_path, image_filename)
            images_with_paths[image.source_path] = new_image_path
        print(images_with_paths)

        return images_with_paths

    def get_output_path(self):
        """
        Gets the output path
        :return: string denoting output path
        """

        if self.seperateOutputPathCheckbox.isChecked():
            output_path = self.outputPathEdit.text()
        else:
            output_path = self.inputPathEdit.text()

        return output_path

    def move_images(self, image_paths):
        """
        Move the images from source to destination path
        """

        image_counter = 0
        for source, destination in image_paths.items():

            # Make directory if it doesn't yet exist
            build_path(destination)

            shutil.move(source, destination)
            image_counter += 1
            self.progressBar.setValue(image_counter)

    def process_images(self):
        """
        Run the image processing.
        """

        output_path = self.get_output_path()
        images = self.read_images()
        image_paths = self.format_to_path(images, output_path)
        self.progressBar.setMaximum(len(images))
        self.move_images(image_paths)

    def enable_disable_output_path_edit(self):
        """
        Enable/disable the output path edit when checkbox is modified
        """

        if self.seperateOutputPathCheckbox.isChecked():
            self.outputPathEdit.setEnabled(True)
            self.outputPathBrowseButton.setEnabled(True)
        else:
            self.outputPathEdit.setDisabled(True)
            self.outputPathBrowseButton.setEnabled(False)


def build_path(path):
    """
    Builds the path for the file
    :param path: File path
    """

    directory_path = os.path.dirname(os.path.realpath(path))
    os.makedirs(directory_path, exist_ok=True)
