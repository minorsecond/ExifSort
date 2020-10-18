"""
Read the image metadata & EXIF data
"""

import pyexiv2


class Image:
    """
    Image class
    """

    def __init__(self, path):
        self.source_path = path
        missing_tag = "unknown"  # What to return if tag is not available
        img = pyexiv2.ImageMetadata(self.source_path)
        img.read()

        # Get the tags
        try:
            self.camera_make = img["Exif.Image.Make"].value
        except KeyError:
            print(f"Missing camera make tag")
            self.camera_make = missing_tag
        try:
            self.camera_model = img["Exif.Image.Model"].value
        except KeyError:
            print(f"Missing camera model tag")
            self.camera_model = missing_tag
        try:
            self.camera_orientation = img["Exif.Image.Orientation"].value
        except KeyError:
            print(f"Missing camera orientation tag")
            self.camera_orientation = missing_tag
        try:
            self.camera_serial_num = img["Exif.Photo.BodySerialNumber"].value
        except KeyError:
            print(f"Missing body serial number tag")
            self.camera_serial_num = missing_tag
        try:
            self.x_resolution = img["Exif.Photo.FocalPlaneXResolution"].value
        except KeyError:
            print(f"Missing x resolution tag")
            self.x_resolution = missing_tag
        try:
            self.y_resolution = img["Exif.Photo.FocalPlaneYResolution"].value
        except KeyError:
            print(f"Missing y resolution tag")
            self.y_resolution = missing_tag
        try:
            self.exposure_time = img["Exif.Photo.ExposureTime"].value
        except KeyError:
            print(f"Missing exposure time tag")
            self.exposure_time = missing_tag
        try:
            self.iso = img["Exif.Photo.ISOSpeedRatings"].value
        except KeyError:
            print(f"Missing ISO tag")
            self.iso = missing_tag
        try:
            self.datetime = img["Exif.Photo.DateTimeOriginal"].value.strftime('%Y-%m-%d_%H-%M-%S')
        except KeyError:
            print(f"Missing datetime tag")
            self.datetime = missing_tag
        try:
            self.aperture_value = img["Exif.Photo.ApertureValue"].value
        except KeyError:
            print(f"Missing aperture value tag")
            self.aperture_value = missing_tag
        try:
            self.meter_mode = img["Exif.Photo.MeteringMode"].value
        except KeyError:
            print(f"Missing meter mode tag")
            self.meter_mode = missing_tag
        try:
            self.image_number = img["Exif.Image.ImageNumber"].value
        except KeyError:
            print(f"Missing image number tag")
            self.image_number = missing_tag
        try:
            self.exposure_mode = img["Exif.Photo.ExposureMode"].value
        except KeyError:
            print(f"Missing exposure mode tag")
            self.exposure_mode = missing_tag
        try:
            self.white_balance = img["Exif.Photo.WhiteBalance"].value
        except KeyError:
            print(f"Missing white balance tag")
            self.white_balance = missing_tag
        try:
            self.lens_make = img["Exif.Photo.LensMake"].value
        except KeyError:
            print(f"Missing lens make tag")
            self.lens_make = missing_tag
        try:
            self.lens_model = img["Exif.Photo.LensModel"].value
        except KeyError:
            print(f"Missing lens model tag")
            self.lens_model = missing_tag
        try:
            self.lens_serial_num = img["Exif.Photo.LensSerialNumber"].value
        except KeyError:
            print(f"Missing lens serial number tag")
            self.lens_serial_num = missing_tag
