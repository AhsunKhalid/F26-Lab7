# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.

# TO DO 2: Create a series according to instructions given in readme.md file.

# TO DO 3: Perform the operations on this series given in readme.md file.

# TO DO 4: Run the script.


# Creating a 2D NumPy array

#STUFF FOR LAB 7d
import numpy as np
arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])
slice_1=arr_2d[0:2,-3:]
print("first two rows and last three columns\n", slice_1)
middle=arr_2d[1:3,1:3]
print("middle 2x2 subarray\n"middle)
slice3=arr_2d[::2,::2]
print("Printing every other row and every other column\n",slice3)

#STUFF FOR 7e
import panda as pd
grade_list=["<50","50-59", "60-69", "70-79", "80-89", "90-100"]
grades=pd.Series(grade_list,index=["F", "D", "C", "B", "A", "A+"])
print(grades)
print(grades("C"))
print(grades.loc[["C","A+"]])
print(grades.iloc[2])
print(grades*3)