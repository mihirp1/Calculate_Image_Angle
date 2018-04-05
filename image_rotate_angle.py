import csv
import math

if __name__ == "__main__":
 row_counter = 0
 column_counter = 0
 list_of_grid_elements = []
 main_list = []
 
 with open("rotated.csv",'r') as f:
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
 for single_element in main_list:
  #print("checking")
  if single_element[2] == 1:
   #print("yes")
   co_ordinates_of_shape.append(single_element)

 #print(len(co_ordinates_of_shape))


 
 
