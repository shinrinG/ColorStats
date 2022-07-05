import configparser
import os
import errno

class Config:
    _path=""
    m_root=""
    m_out=""
    m_img_w=256
    m_img_h=256
    m_img_c=3
    m_img_ext="bmp"
    m_patch_w = 128
    m_patch_h = 128
    m_roi_x = 0
    m_roi_y = 0
    m_roi_w = 1024
    m_roi_h = 1024

    _bOK = True

    def __init__(self,filepath):
        self._path = filepath
        ini = configparser.ConfigParser()
        if not os.path.exists(self._path):
            self._bOK = False
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self._path)
        ini.read(self._path,encoding='utf-8')
        self.m_root=ini["System"]["ROOT_FOLDER"]
        self.m_root=ini["System"]["OUTPUT_FOLDER"]
        self.m_img_h=int(ini["Input"]["IMG_HEIGHT"])
        self.m_img_w=int(ini["Input"]["IMG_WIDTH"])
        self.m_img_c=int(ini["Input"]["IMG_COLOR"])
        self.m_img_ext=ini["Input"]["IMG_EXT"]
        self.m_patch_w=int(ini["Imgproc"]["PATCH_WIDTH"])
        self.m_patch_h=int(ini["Imgproc"]["PATCH_HEIGHT"])
        self.m_roi_x=int(ini["Imgproc"]["ROI_X"])
        self.m_roi_y=int(ini["Imgproc"]["ROI_Y"])
        self.m_roi_w=int(ini["Imgproc"]["ROI_W"])
        self.m_roi_h=int(ini["Imgproc"]["ROI_H"])

    def check(self):
        return self._bOK