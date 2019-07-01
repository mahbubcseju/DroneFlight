import math
import matplotlib.pyplot as plot
class DisplayUtil:
    def __init__(self,sweep_points,flight_points):
        """
        Constructor of DisplayUtil class

        @param sweep_points: A list with angle and distance of all sweep.
        @param flight_points: Collection of the flight points.
        """
        self.sweep_points=sweep_points
        self.flight_points=flight_points

    def plot_sweep(self,x_axis_list,y_axis_list,sweep_number):

        """
        This function plot a sweep boundary points as well as that sweep's lidar
        point. Plot the lidar position with green color and Plot the sweep's points
        with red color.

        @param x_axis_list: List of x axis points of the sweep boundary points.
        @param y_axis_list: List of y axis points of the sweep boundary points.
        @param sweep_number: Sweep number which boundary is to be plotted.
        """
        plot.figure(sweep_number)
        plot.scatter(x_axis_list, y_axis_list, c='r')
        plot.scatter([self.flight_points[sweep_number][0]],[self.flight_points[sweep_number][1]], c='g')
        plot.show()

    def display_sweep(self):


        """
        Calculate all  co-ordinates(xi,yi) of each sweep boundary using angle and distance
        based on the lidar's position(x,y).
        1. Convert the angle from degree to redian using the following formula.
               redian= (pi* degree)/180
        2. Then find the co-ordinate at distance d and angle e  using formula.
               xi=x+d * cos(e)
               yi=y+d * sin(e)
           where (x,y) is current lidar's position.
        3. Finally call the plot sweep function to plot these co-ordinates.
        """
        for sweep in range(len(self.sweep_points)):
            lidar_x_coordinate=self.flight_points[sweep][0]
            lidar_y_coordinate=self.flight_points[sweep][1]

            xx=[]
            yy=[]
            for point in range(len(self.sweep_points[sweep])):
                angle_degree=self.sweep_points[sweep][point][0]
                distance=self.sweep_points[sweep][point][1]
                angle_redian = (math.pi * angle_degree) / 180.0
                sweep_point_x=lidar_x_coordinate+ (distance * math.cos(angle_redian))/1000.0
                sweep_point_y=lidar_y_coordinate+ (distance * math.sin(angle_redian))/1000.0
                xx.append(sweep_point_x)
                yy.append(sweep_point_y)

            self.plot_sweep(xx,yy,sweep)

