# DroneFlight

My main target here is to provide an appropriate visualization of drone's path and the Lidar data. I will here show each sweep of data in isolation as well as all the sweeps combined together. Also another target is to find a better flight path that will result in the shortest possible time but still goes through the existing rooms based on the provided data.


## Work Breakdown

### Display sweep
1. Read and Preprocess data.
2. Display each sweep.

### Flight Optimization
1. Read and Preprocess data.
2. Optimizing the path.
3. Write the optimized path in CSV file and return.


### Methodology

#### 1. Display sweep
        - Read LIDAR data and flight path data from csv file.
        - Convert LIDAR data to two dimensional list such that each row contains the data of one sweep.
        - Iterate through  each sweep.
        - Extract the LIDAR position (x,y) from flight Path file for current sweep.
        - Calculate all the co-ordinates (xi,yi) of current sweep boundary using angle and distance by the following formula.
              xi = x + distance * cos(angle)
              yi = y+  distance * sin(angle)
        - Store all the xi in a list and yi in another list.
        - Display the sweep using the two calculated list by matplotlib library.
        - Also plot the postion of LIDAR/Drone .
        - LIDAR/Drone position is marked by  green color and sweep boundary is marked by red color.

##### 2. Flight Optimization
