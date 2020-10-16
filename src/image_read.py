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
        print("Opening " + path)
        img = pyexiv2.ImageMetadata(self.source_path)
        img.read()

        # Get the tags
        try:
            self.camera_make = img["Exif.Image.Make"]
            self.camera_model = img["Exif.Image.Model"]
            self.camera_orientation = img["Exif.Image.Orientation"]
            self.camera_serial_num = img["Exif.Photo.BodySerialNumber"]
            self.x_resolution = img["Exif.Photo.FocalPlaneXResolution"]
            self.y_resolution = img["Exif.Photo.FocalPlaneYResolution"]
            self.exposure_time = img["Exif.Photo.ExposureTime"]
            self.iso = img["Exif.Photo.ISOSpeedRatings"]
            self.datetime = img["Exif.Photo.DateTimeOriginal"]
            self.aperture_value = img["Exif.Photo.ApertureValue"]
            self.meter_mode = img["Exif.Photo.MeteringMode"]
            self.image_number = img["Exif.Image.ImageNumber"]
            self.exposure_mode = img["Exif.Photo.ExposureMode"]
            self.white_balance = img["Exif.Photo.WhiteBalance"]
            self.lens_make = img["Exif.Photo.LensMake"]
            self.lens_model = img["Exif.Photo.LensModel"]
            self.lens_serial_num = img["Exif.Photo.LensSerialNumber"]

        except KeyError as e:
            print(f"Missing key in Exif data: {e}")
