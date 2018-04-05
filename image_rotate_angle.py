import csv
import math

if __name__ == "__main__":
 row_counter = 0
 column_counter = 0
 list_of_grid_elements = []
 main_list = []
 
 with open('rotated.csv','r') as f:
    with open("rotated_updated.csv",'w') as f1:
        f.readline() # skip header line
        for line in f:
            f1.write(line) 


 with open('rotated_updated.csv', 'r') as f:
  reader = csv.reader(f)
  for row_number,column in enumerate(reader):
   #if(row_number != 0):
    #print(column)
    #break
    for column_number,element in enumerate(column):
     #print(row_number,column_number,column[column_number])
     if(not element.startswith('V')):
      list_of_grid_elements.append(int(row_number)+1)
      list_of_grid_elements.append(int(column_number)+1)
      list_of_grid_elements.append(int(column[column_number]))
      main_list.append(list_of_grid_elements)
      list_of_grid_elements  = []
      #print(list_of_grid_elements)
      #print(column[0]) 
 print(len(main_list))
 print(main_list)

 


##Return Co=ordinates of the Dark Image 
 co_ordinates_of_shape = []
 four_corners_of_rectangle = []
 single_point_coordinates = []
 for single_element in main_list:
  #print("checking")
  if single_element[2] == 1:
   #print("yes")
   co_ordinates_of_shape.append(single_element)

 #print(len(co_ordinates_of_shape))
 temp_highest_row = 0
 temp_highest_col = 0
 temp_lowest_row = 10000000
 temp_lowest_col = 10000000
 for black_pixel in co_ordinates_of_shape:
  if(black_pixel[0] > temp_highest_row):
   temp_highest_row = black_pixel[0]

  if(black_pixel[0] == temp_highest_row):
   temp_highest_row_cc_col = black_pixel[1]
   Y1,X1 = temp_highest_row, temp_highest_row_cc_col
   #print(temp_highest_row,temp_highest_row_cc_col)
   #single_point_coordinates.append(temp_highest_row)
   #single_point_coordinates.append(temp_highest_row_cc_col)
   #four_corners_of_rectangle.append([temp_highest_row,temp_highest_row_cc_col])

  if(black_pixel[1] > temp_highest_col):
   temp_highest_col = black_pixel[1]

  if(black_pixel[1] == temp_highest_col):
   temp_highest_col_cc_row = black_pixel[0]
   #four_corners_of_rectangle.append([temp_highest_col,temp_highest_col_cc_row])
   

  if(black_pixel[0] < temp_lowest_row):
   temp_lowest_row = black_pixel[0]

  if(black_pixel[0] == temp_lowest_row):
   temp_lowest_row_cc_col = black_pixel[1] 
   #print(temp_lowest_row,temp_lowest_row_cc_col)
   #four_corners_of_rectangle.append([temp_lowest_row,temp_lowest_row_cc_col])

  if(black_pixel[1] < temp_lowest_col):
   temp_lowest_col = black_pixel[1]

  if(black_pixel[1] == temp_lowest_col):
   temp_lowest_col_cc_row = black_pixel[0]
   #print(temp_lowest_col,temp_lowest_col_cc_row)
   #four_corners_of_rectangle.append([temp_lowest_col,temp_lowest_col_cc_row])
   Y2,X2 = temp_lowest_col_cc_row,temp_lowest_col
 print(temp_highest_row,temp_highest_col,temp_lowest_row,temp_lowest_col)
 
 #print(temp_highest_row,temp_highest_row_cc_col)
 #print(temp_highest_col_cc_row,temp_highest_col)
 #print(temp_lowest_row,temp_lowest_row_cc_col)
 #print(temp_lowest_col_cc_row,temp_lowest_col)
 #print(math.degrees(math.atan(-188/140)))

 '''
 four_corners_of_rectangle.append([temp_highest_row,temp_highest_row_cc_col])
 four_corners_of_rectangle.append([temp_highest_col,temp_highest_col_cc_row])
 four_corners_of_rectangle.append([temp_lowest_row,temp_lowest_row_cc_col])
 four_corners_of_rectangle.append([temp_lowest_col,temp_lowest_col_cc_row])

 #print(four_corners_of_rectangle)
 
 l_poi_slo = []
 angles = []
 ##Looking For Same Slopes/Parallel Lines 
 for p in four_corners_of_rectangle:
  for pp in four_corners_of_rectangle:
   if(p is not pp):
    slope = ((p[1]-pp[1])/p[0]-pp[0])
    angle_presently = math.degrees(math.atan(slope))
    l_poi_slo.append([p,pp,int(round(angle_presently))])
    angles.append(int(round(angle_presently)))
 print(l_poi_slo)  
 
 angle_list = list(set(angles))
 print(angle_list)
 #Looking for DIfferent Points :
 one_set_of_points = []
 second_set_of_points = []
 for point in l_poi_slo:
  for s_point in l_poi_slo:
   if(point[2] != s_point[2] and abs(point[2] - s_point[2]) < 2):
    x1,y1 = point[0]
    x2,y2 = point[1]
 '''
 slope = (Y2-Y1)/(X2-X1)

 #Since we are considering always the lowest column and highest row, rotation is always Clockwise 

 print(math.degrees(math.atan(-188/140)) * -1) 
