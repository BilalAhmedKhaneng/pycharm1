#we can make folden manually like harry python code


import os
if(not os.path.exists("data")):
 os.mkdir("data")

for i in range (0,100):
    os.mkdir(f"data/day(i+1)")
    #we can rename the folder also

