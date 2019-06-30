# DroneFlight

My main target here is to provide an appropriate visualization of drone's path and the Lidar data. I will here show each sweep of data in isolation as well as all the sweeps combined together. Also another target is to find a better flight path that will result in the shortest possible time but still goes through the existing rooms based on the provided data.


## Work Breakdown

### Display sweep
1. Read and Pre-process data.
2. Display each sweep.

### Flight Optimization
1. Read and Pre-process data.
2. Optimizing the path.
3. Write the optimized path in CSV file and return.


## Methodology

### 1. Display sweep
        - Read LIDAR data and flight path data from csv file.
        - Convert LIDAR data to two dimensional list such that each row contains the data of one sweep.
        - Iterate through  each sweep.
        - Extract the LIDAR position (x,y) from flight Path file for current sweep.
        - Calculate all the co-ordinates (xi,yi) of current sweep boundary using angle and distance by the 
          following formula.
              xi = x + distance * cos(angle)
              yi = y+  distance * sin(angle)
        - Store all the xi in a list and yi in another list.
        - Display the sweep using the two calculated list by matplotlib library.
        - Also plot the postion of LIDAR/Drone .
        - LIDAR/Drone position is marked by  green color and sweep boundary is marked  by red color.

#### 2. Flight Optimization
         - Read LIDAR data and flight path data from csv file.
         - Convert LIDAR data to two dimensional list such that each row contains the data of one sweep.
         - I traverse through the path.
         - When  I am  at position of index i, I tried to find wheather is there any way to  go at position of
           index j (all j such that j>i) by straight line. 
         - For each i, we check continously upto the last ending position.
         - When I find any position of index j which is not reachable from position  of index i, I don't check
           for the rest position after j. If position of index j is not reachable by straight line ,then I co-
           nsider that position of index (j+1) is not reachable by straight line.
         - After position of index i, I directly go to position of index position of index j as position of 
           index j is reachable from position of index  i.
         - So I just ommit all the position between index i and j.
         - After that I update  i using j.
         - I insert the position of each i in a list and finally return that list.
         