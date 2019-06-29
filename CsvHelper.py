import csv

class CsvHelper:
    def __init__(self,lidar_file,flight_file):
        """
        @param lidar_file: given or generated LIDARPoint.csv file's path
        @param flight_file: given or generated FlightPath.csv file's path

        Constructor of CsvHelper Class
        """
        self.lidar_file=lidar_file
        self.flight_file=flight_file

    def make_list(self,x,y):
        """
        @param x: An integer or float element
        @param y: An integer or float element

        @Return: return a list whose elements are x,y
        """
        result_list = []
        result_list.append(x)
        result_list.append(y)
        return result_list

    def read_lidar_element(self):
        """
        Read given or pre-generated lidar points
        @Return lidar_points: Return a two dimensional list of lidar point.
                              Each row contains the point of a distinct sweep
        """
        with open(self.lidar_file) as lidar_reader:
            read_lidar_point = csv.reader(lidar_reader, delimiter=',')
            temp_lidar_points=[]
            for points in read_lidar_point:
                temp_lidar_points.append(points)

            ptr=0;
            lidar_points=[]
            while ptr<len(temp_lidar_points):
                current_sweep_length = int(temp_lidar_points[ptr][1])
                current_sweep_points=[]
                for point in range(ptr+1,ptr+current_sweep_length+1):
                    current_sweep_points.append(self.make_list(float(temp_lidar_points[point][0]),float(temp_lidar_points[point][0])))

                ptr=ptr+current_sweep_length+1
                lidar_points.append(current_sweep_points)
            return lidar_points

    def read_flight_path_element(self):
        """
        Read given or pre-generated flight path co-oridnates
        @Return flight_points: Return a two dimensional list of flight points.
                              Each row contains the points of a distinct sweep
        """
        with open(self.flight_file) as flight_reader:
            read_flight_point = csv.reader(flight_reader, delimiter=',')
            temp_flight_points=[]
            for points in read_flight_point:
                temp_flight_points.append(points)

            flight_points=[]
            for point in range(len(temp_flight_points)):
                if point%2==1:
                    flight_points.append(self.make_list(float(temp_flight_points[point][0]),float(temp_flight_points[point][1])))
            return flight_points