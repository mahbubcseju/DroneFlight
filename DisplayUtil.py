import math
import matplotlib.pyplot as plot
class DisplayUtil:
    def __init__(self,sweep_points,flight_points):
        """
        @param sweep_points: angle and distance of each sweep
        @param flight_points: Collection of the flight points

        Constructor of DisplayUtil class
        """
        self.sweep_points=sweep_points
        self.flight_points=flight_points

    def plot_sweep(self,x_axis_list,y_axis_list,sweep_number):

        """
        Plot a sweep points as well as that sweep's lidar point
        plot the lidar position with green color
        plot the sweep's points with red color
        """
        plot.figure(sweep_number)
        plot.scatter(x_axis_list, y_axis_list, c='r')
        plot.scatter([self.flight_points[sweep_number][0]],[self.flight_points[sweep_number][1]], c='g')
        plot.show()

    def display_sweep(self):


        """
        Calculate all  co-ordinates of each sweep using angle and distance based on the lidar's position
        1. Convert the angle from degree to redian using the following formula
               redian= (pi* degree)/180
        2. then find the co-ordinate at distance d and angle e  using formula
               x1=x+d * cos(e)
               y1=y+d * sin(e)
           where (x,y) is current lidar position.
        3. Final divide
        Then plot these co-ordinates
        """
        for sweep in range(len(self.sweep_points)):
            lidar_x_coordinate=self.flight_points[sweep][0]
            lidar_y_coordinate=self.flight_points[sweep][1]

            xx=[]
            yy=[]
            for point in range(len(self.sweep_points[sweep])):
                angle_degree=self.sweep_points[sweep][point][0]
                distance=self.sweep_points[sweep][point][1]

                print(angle_degree,distance)
                angle_redian = (math.pi * angle_degree) / 180.0
                print(lidar_x_coordinate,lidar_y_coordinate,angle_redian,distance)
                sweep_point_x=lidar_x_coordinate+ (distance * math.cos(angle_redian))/1000.0
                sweep_point_y=lidar_y_coordinate+ (distance * math.sin(angle_redian))/1000.0
                print(sweep_point_y, sweep,sweep_point_y)
                xx.append(sweep_point_x)
                yy.append(sweep_point_y)

            self.plot_sweep(xx,yy,sweep)

