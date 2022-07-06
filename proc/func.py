import copy
import numpy as np
import cv2
from utils.Rect import Rect
from utils.ResPack import ResPack
# get mean 
def get_color(src:cv2.Mat):
    col1 = src.T[0].flatten().mean()
    col2 = src.T[1].flatten().mean()
    col3 = src.T[2].flatten().mean()
    return col1,col2,col3

def get_color_patchwise(impath:str,w_patch:int,h_patch:int, area:Rect):
    res_arr = np.zeros((1,8))
    m_img_bgr = cv2.imread(impath,cv2.IMREAD_COLOR)
    m_img_hsv = cv2.cvtColor(m_img_bgr,cv2.COLOR_BGR2HSV)
    m_img_lab = cv2.cvtColor(m_img_bgr,cv2.COLOR_BGR2Lab)
    
    ini_x,ini_y = area.pos_LU()
    end_x,end_y = area.pos_RB()
    m_roi_hsv = m_img_hsv[ini_y:end_y,ini_x:end_x]
    m_roi_lab = m_img_lab[ini_y:end_y,ini_x:end_x]

    num_w = (end_x-ini_x)//w_patch
    num_h = (end_y-ini_y)//h_patch

    c_rp = ResPack()
    for x in range(num_w):
        for y in range(num_h):
            c_rp.set_xy(x,y)
            c_roi_hsv = m_roi_hsv[y*h_patch:(y+1)*h_patch,x*w_patch:(x+1)*w_patch]
            c_roi_lab = m_roi_lab[y*h_patch:(y+1)*h_patch,x*w_patch:(x+1)*w_patch]
            h,s,v = get_color(c_roi_hsv)
            l,a,b = get_color(c_roi_lab)
            c_rp.set_hsv(h,s,v)
            c_rp.set_lab(l,a,b)
            c_arr = copy.deepcopy(c_rp.get_arrays())
            res_arr = np.append(res_arr,c_arr,axis=0)
    return res_arr[1:] #0行目捨てる




