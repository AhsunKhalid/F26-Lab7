# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

# TO DO 1: Create numArray according to instructions given in readme.md file.

# TO DO 2: Perform the operations on numArray given in readme.md file.

# TO DO 3: Run the script.

import numpy as np
arr=np.random.rand(100)
slice_1=arr[:10]
print("\nfirst 10 values of Sliced 1D Array:", slice_1)
slice_2=arr[-10:]
print("\nfirst 10 values of Sliced 1D Array:", slice_2)
slice_3=arr[-21:]
print("\n30 values steating from index 21 of 1D Array:", slice_3)
np.out(arr,[num for num in range(50,66) [101]])
print("\nnew values at index 50 to 65 of 1D array", arr[50:66])
