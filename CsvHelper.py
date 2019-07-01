import csv

class CsvHelper:
    def __init__(self,lidar_file,flight_file):
        """
        This function is the constructor of CsvHelper Class.

        @param lidar_file: given or generated LIDARPoint.csv file's path.
        @param flight_file: given or generated FlightPath.csv file's path.
        """
        self.lidar_file=lidar_file
        self.flight_file=flight_file

    def make_list(self,x,y):
        """
        This function creates a list of two element.

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
        This function reads given or pre-generated lidar points and create
        a two dimensional list of lidar point. Each row contains the point
        of a distinct sweep.

        @Return lidar_points: Return a two dimensional list of lidar point.
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
                    current_sweep_points.append(self.make_list(float(temp_lidar_points[point][0]),float(temp_lidar_points[point][1])))

                ptr=ptr+current_sweep_length+1
                lidar_points.append(current_sweep_points)
            return lidar_points

    def read_flight_path_element(self):
        """
        This function reads given or pre-generated flight path co-oridnates
        and make a two dimensional list of flight points. Each row contains
        the points of a distinct sweep

        @Return flight_points: Return a two dimensional list of flight points.
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


    def write_csv(self,data,file_name_csv):
        """
        This function writes data on csv format in a csv file .

        @param data: Given data which is going to be written in csv file.
        @param file_name_csv: Csv file name in which data will be written.
        """
        with open(file_name_csv, "w") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def write_flight_path(self,flight_path,output_flight_csv):
        """
        This function pre-process the flight path points and call
        the write_csv function to write data on a given csv file.
        In the given flight_path list, only the co-ordinates
        are given. Sweep number are not included. So this function
        add one additional line/list [sweep number,1] before each flight
        co-ordinate and call write_csv to write these data on the file.

        @param flight_path: Flight path points/co-ordinates
        @param output_flight_csv: File name in which flight path points
                                 will be written.
        """
        output_flight_path=[]
        for point  in range(len(flight_path)):
            output_flight_path.append(self.make_list(point,1))
            output_flight_path.append(flight_path[point])
        self.write_csv(output_flight_path,output_flight_csv)