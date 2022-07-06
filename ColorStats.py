import os
import numpy as np
from shutil import ReadError
from utils.IniFile import Config
from utils.utils import find_all_files,get_curtime,make_dir
from utils.Rect import Rect
from proc.func import get_color_patchwise

INI = ".\\Config.ini"
APP_NAME = "ColorStats"
VERSION = "0.9.0.0"

#Main Proc
if __name__ == "__main__":
    ini_show = APP_NAME + " ver " + VERSION
    print(ini_show)

    # Read ini
    print("read ini ...\n")
    cfg = Config(INI)
    timetag = get_curtime()

    # Read files
    print("find file ...\n")
    imgs = find_all_files(cfg.m_root,cfg.m_img_ext)

    #improc all images
    print("proces ...\n")
    res_dict = {}
    roi = Rect(
        cfg.m_roi_x,
        cfg.m_roi_y,
        cfg.m_roi_w,
        cfg.m_roi_h
        )
    for img in imgs:
        c_key = os.path.basename(img)[:-4]
        c_val = get_color_patchwise(
            img,
            cfg.m_patch_w,
            cfg.m_patch_h,
            roi
            )
        res_dict[c_key] = c_val
    
    #all result out
    print("create result ...\n")
    o_folder = cfg.m_out + "\\" + timetag
    make_dir(o_folder)
    header_txt = "x,y,h,s,v,l,a,b"

    for k,v in res_dict.items():
        csv_path = o_folder + "//" + k + ".csv"
        np.savetxt(csv_path, v, delimiter=',',header=header_txt)
    
    print("all done.")

    




