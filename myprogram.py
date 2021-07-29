
# importing function module
import sys
sys.path.append("/home/cavid/Desktop/Alienide/All_project/python/modules")

import functions as fn


area = fn.calculator_square_area(15)
print(area)

# 
bitcoin = fn.bitcoin_cal_bd(10000,3.5e-7)
print("bitcoin price in BDT", bitcoin)
