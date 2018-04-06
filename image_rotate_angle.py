# Author: Mihir Phatak
# Date: April 07, 2018
# Purpose: QuantumScape Software Engineering Intern Coding Challenge 
# Title : Binary Image Rotation Angle Getter in CSV

import csv
import math

def find_correction_angle(input_csv_file):
 row_counter = 0
 column_counter = 0
 list_of_grid_elements = []
 main_list = []
 updated_csv_file = input_csv_file + '_updated.csv'
 
 with open(input_csv_file,'r') as f:
    with open(updated_csv_file,'w') as f1:
       f.readline() 
       for line in f:
           f1.write(line) 


 with open(updated_csv_file, 'r') as f:
  reader = csv.reader(f)
  for row_number,column in enumerate(reader):
    for column_number,element in enumerate(column):
     if(not element.startswith('V')):
       list_of_grid_elements.append(int(row_number)+1)
       list_of_grid_elements.append(int(column_number)+1)
       list_of_grid_elements.append(int(column[column_number]))
       main_list.append(list_of_grid_elements)
       list_of_grid_elements  = []
 print(len(main_list))
 print(main_list)

 ##Return Co=ordinates of the Dark Image 
 co_ordinates_of_shape = []
 four_corners_of_rectangle = []
 single_point_coordinates = []
 for single_element in main_list:
  if single_element[2] == 1:
   co_ordinates_of_shape.append(single_element)

 temp_highest_row = 0
 temp_highest_col = 0
 temp_lowest_row = 10000000
 temp_lowest_col = 10000000
 for black_pixel in co_ordinates_of_shape:
  if(black_pixel[0] > temp_highest_row):
   temp_highest_row = black_pixel[0]

  if(black_pixel[0] == temp_highest_row):
   temp_highest_row_cc_col = black_pixel[1]
   Y1,X1 = temp_highest_row, temp_highest_row_cc_col #Point with highest row co-ordinate (y co-ordinate)

  if(black_pixel[1] > temp_highest_col):
   temp_highest_col = black_pixel[1]

  if(black_pixel[1] == temp_highest_col):
   temp_highest_col_cc_row = black_pixel[0]

  if(black_pixel[0] < temp_lowest_row):
   temp_lowest_row = black_pixel[0]

  if(black_pixel[0] == temp_lowest_row):
   temp_lowest_row_cc_col = black_pixel[1] 

  if(black_pixel[1] < temp_lowest_col):
   temp_lowest_col = black_pixel[1]

  if(black_pixel[1] == temp_lowest_col):
   temp_lowest_col_cc_row = black_pixel[0]
   Y2,X2 = temp_lowest_col_cc_row,temp_lowest_col #Point with lowest column co-ordinate (x co-ordinate)
 print(temp_highest_row,temp_highest_col,temp_lowest_row,temp_lowest_col)
 

 slope = (Y2-Y1)/(X2-X1) # Calculating Slope from two leftmost points

 #Since we are considering always the lowest column and highest row, we are always looking at the edge of the rectangle with the positive slope, 
 #As a result, rotation is always Clockwise and angle always positive 

 print(math.degrees(math.atan(slope)))


if __name__ == "__main__":
 input_csv_file = "rotated.csv"
 find_correction_angle(input_csv_file)

