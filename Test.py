from CsvHelper import CsvHelper
from DisplayUtil import DisplayUtil
from Optimization import Optimization

def test_optimization(lidar_points_file_name,flight_path_file_name):
    """
    This function is used to display each sweep one by one of the optimized
    flight path. This function first read_lidar_element() and read_flight_element()
    functions from CsvHelper class to read the lidar's point and flight path points
    from given csv file. Then it calls optimization function from Optimization class
    to optimize the flight path. After that it calls display_sweep function from
    DisplayUtil class to display each sweep one by one of the optimized flight path.

    @param lidar_points_file_name: Given file name of lidar's point.
    @param flight_path_file_name:  Given file name of flight path points.
    """
    csv_helper=CsvHelper(lidar_points_file_name,flight_path_file_name)
    flight_path=csv_helper.read_flight_path_element()
    lidar_points=csv_helper.read_lidar_element()
    if len(flight_path)!=len(lidar_points):
        print("Wrong given data! Number of sweep in booth file is not equal")
    else:
        optimization=Optimization(lidar_points,flight_path)
        optimized_lidar_points,optimized_flight_path=optimization.optimization()
        display_helper=DisplayUtil(optimized_lidar_points,optimized_flight_path)
        display_helper.display_sweep()

