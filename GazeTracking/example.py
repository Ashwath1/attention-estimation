"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import sys
import xlwt
import time
import cv2
import xlsxwriter,pandas
from gaze_tracking import GazeTracking
from evaluate_sheet import _process_sheet

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
TT = 25  #number of frames it is going to run
wb = xlsxwriter.Workbook(r'C:\Users\dvk\Desktop\MajorProject-main\GazeTracking\hrvr_table.xlsx')
sheet = wb.add_worksheet('hrvr_table')
c0 = 0
c1 = 1
c2 = 2
i = 0

row=0
column=0

while TT > 0:
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    cv2.imshow("Demo", frame)
    hr=gaze.horizontal_ratio()
    vr=gaze.vertical_ratio()
    l=[]
    l.append(hr)
    l.append(vr)
    

    print(gaze.horizontal_ratio(),gaze.vertical_ratio())
    for x in l:
        sheet.write(row,column,x)
        column+=1
    row+=1
    column=0
    # sheet.write(i,c0,gaze.horizontal_ratio()) #first row
    # sheet.write(i,c1,gaze.vertical_ratio())   #second row
    TT = TT - 1
    i = i + 1
    time.sleep(0.5)
    if cv2.waitKey(1) == 27:
        break

# wb.save('hrvr_table.xls')
wb.close()
# _process_sheet()