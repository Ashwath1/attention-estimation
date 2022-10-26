import pandas as pd
import numpy as np
import xlsxwriter

                    
standard_frames = 120
#column numbers
c0 = 0
c1 = 1
c2 = 2
c3 = 3
c4 = 4
row_counter = 0

#sheet variables
sheet = None
hr = []
vr = []

#read the excel sheet as a data frame
with pd.ExcelFile("hrvr_table.xlsx") as reader:
    sheet = pd.read_excel(reader, sheet_name = 'hrvr_table')
data = sheet.to_numpy() #convert to np array
print(data)
#strip the values to horizontal and vertical to individual lists
for i in data:
    hr.append(i[0])
    vr.append(i[1])
#lists are ready
# print(hr,vr,end=" ")
wb = xlsxwriter.Workbook(r'C:\Users\dvk\Desktop\MajorProject-main\GazeTracking\hrvr_table_evaluate.xlsx')
eval_sheet = wb.add_worksheet('hrvr_table_evaluate')
frames = 1
average_hr = 0
average_vr = 0
sum_hr = 0
sum_vr = 0
nan_hr = 0
nan_vr = 0
for i in range(len(hr)):
    if(frames == standard_frames):
        if(nan_vr > 40 or nan_hr > 40): # more than 1/3 of time was spent undetected, so deem the frame unecessary
            try:
                eval_sheet.write(row_counter,c3,-1)
                eval_sheet.write(row_counter,c4,-1)
            except:
                pass
        else:
        #calculate averages
        #log the averages in to the excel sheet
            average_hr = sum_hr / (frames - (nan_hr)) #ignore the number of time the model did not detect of person not found
            average_vr = sum_hr / (frames - (nan_vr)) # fix this bug later
            try:
                eval_sheet.write(row_counter,c3,average_hr)
                eval_sheet.write(row_counter,c4,average_vr)
            except:
                pass

        row_counter = row_counter + standard_frames
        nan_hr = 0
        nan_vr = 0
        sum_hr = 0
        sum_vr = 0
        frames = 0
    if(hr[i] == np.nan):
        nan_hr = nan_hr + 1
        frames = frames + 1
    elif(vr[i] == np.nan):
        nan_vr = nan_vr + 1
        frames = frames +1
    else:
        sum_hr = sum_hr + hr[i]
        sum_vr = sum_vr + vr[i]
        frames = frames + 1
#log the rest of the data after the loop ends, might have less than 120 frames captured
average_hr = sum_hr / (frames - (nan_hr)) 
average_vr = sum_hr / (frames - (nan_vr)) 
try:
    eval_sheet.write(row_counter,c3,average_hr)
    eval_sheet.write(row_counter,c4,average_vr)
except:
    pass
wb.close()