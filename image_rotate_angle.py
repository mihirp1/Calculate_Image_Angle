# Author: Mihir Phatak
# Date: April 07, 2018
# Purpose: QuantumScape Software Engineering Intern Coding Challenge 
# Title : Binary Image Rotation Angle Getter in CSV without using numpy
# Program Language : Python3

import csv                                        #Used to Read data from CSV File
import math                                       #Used for calculating tan-inverse of slope of a rectangle edge
import sys                                        #Used for accepting commadnline argument as the input CSV File

#Function That Returns  Correction Angle
def find_correction_angle(input_csv_file):
 row_counter = 0
 column_counter = 0
 list_of_grid_elements = []
 main_list = []
 updated_csv_file = input_csv_file + '_updated.csv'
 
 with open(input_csv_file,'r') as f:               #Nested Context Manager for reading original CSV File
  with open(updated_csv_file,'w') as f1:
       f.readline() 
       for line in f:
           f1.write(line) 

 with open(updated_csv_file, 'r') as f:            #Nested Context Manager for reading updated CSV file with first row labels removed'''
  reader = csv.reader(f)
  for row_number,column in enumerate(reader):      #Creation Of Three Element List for co-ordinates and values : (X,Y,Pixel-Value)'''
    for column_number,element in enumerate(column):
     if(not element.startswith('V')):
       list_of_grid_elements.append(int(row_number)+1)
       list_of_grid_elements.append(int(column_number)+1)
       list_of_grid_elements.append(int(column[column_number]))
       main_list.append(list_of_grid_elements)
       list_of_grid_elements  = []

 #Return LeftMost Edge Co-ordinates of the Rectangle 
 co_ordinates_of_shape = []
 four_corners_of_rectangle = []
 single_point_coordinates = []
 for single_element in main_list:                   #Seperating Element Point(pixels) of White Shape
  if single_element[2] == 1:
   co_ordinates_of_shape.append(single_element)

 temp_highest_row = 0
 temp_highest_col = 0
 temp_lowest_row = 10000000
 temp_lowest_col = 10000000
 for black_pixel in co_ordinates_of_shape:          #Finding End-Points of Leftmost Edge Of Rectangle

  if(black_pixel[0] > temp_highest_row):
   temp_highest_row = black_pixel[0]

  if(black_pixel[0] == temp_highest_row):
   temp_highest_row_cc_col = black_pixel[1]
   Y1,X1 = temp_highest_row, temp_highest_row_cc_col #Point with highest row co-ordinate (y co-ordinate)

  if(black_pixel[1] < temp_lowest_col):
   temp_lowest_col = black_pixel[1]

  if(black_pixel[1] == temp_lowest_col):
   temp_lowest_col_cc_row = black_pixel[0]
   Y2,X2 = temp_lowest_col_cc_row,temp_lowest_col    #Point with lowest column co-ordinate (x co-ordinate)

 slope = (Y2-Y1)/(X2-X1)                             #Calculating Slope from two leftmost points
 '''
 Since we are considering always the lowest column and highest row, we are always looking at the edge of the rectangle with the positive slope, 
 As a result, rotation is always Clockwise and angle always positive 
 '''
 return(math.degrees(math.atan(slope)))

''' Main Function Accepts Commandline CSV File '''

if __name__ == "__main__": 
 input_csv_file = sys.argv[1]
 correction_angle = find_correction_angle(input_csv_file) 
 print("\nCorrection Angle is : ",correction_angle)
 print("\n")
