import sys

from CsvHelper import CsvHelper
from DisplayUtil import DisplayUtil
from Optimization import Optimization
import Test

def run_display(lidar_points_csv,flight_path_csv):
    """
    This function is used to display each sweep one by one.
    This function first read_lidar_element() and read_flight_element()
    functions from CsvHelper class to read the lidar's point and flight
    path points from given csv file. After that it calls display_sweep
    function from DisplayUtil class to display each sweep one by one.

    @param lidar_points_csv: Given file name of lidar's point.
    @param flight_path_csv:  Given file name of flight path points.
    """
    csv_helper=CsvHelper(lidar_points_csv,flight_path_csv)
    lidar_points = csv_helper.read_lidar_element()
    flight_path = csv_helper.read_flight_path_element()
    display_helper=DisplayUtil(lidar_points,flight_path)
    display_helper.display_sweep()



def run_flight_optimization(lidar_points_csv,flight_path_csv,output_flight_path_csv):
    """
    This function is used to optimize the flight path.
    This function first read_lidar_element() and read_flight_element()
    functions from CsvHelper class to read the lidar's point and flight
    path points from given csv file. After that it calls optimization function
    from Optimization class. Finally it calls write_flight_path functions from
    CsvHelper class to write optimized flight path  in the given file name.

    @param lidar_points_csv: Given file name of lidar's point.
    @param flight_path_csv:  Given file name of flight path points.
    @param output_flight_path_csv: Given file name to write optimized
                                   flight path.
    """
    csv_helper=CsvHelper(lidar_points_csv,flight_path_csv)
    lidar_points = csv_helper.read_lidar_element()
    flight_path = csv_helper.read_flight_path_element()

    optimization = Optimization(lidar_points, flight_path)
    optimized_lidar_points, optimized_flight_path = optimization.optimization()
    csv_helper.write_flight_path(optimized_flight_path,output_flight_path_csv)

def print_log():

    print("     For display, run: python droneflight.py --dis \"LIDARDPoints.csv\" \"FlightPath.csv\" ")
    print(
        "     For flight ptimization, run: python droneflight.py --op \"LIDARDPoints.csv\" \"FlightPath.csv\" \"OutputFlightPath.csv\"")
    print("     For Testing optimization, run: python droneflight.py --test \"LIDARDPoints.csv\" \"FlightPath.csv\" ")
    print("     Please change \"LIDARDPoints.csv\" and \"FlightPath.csv\" based on your input file")

if(len(sys.argv)>=2):
    action = sys.argv[1]
    filenames = sys.argv[2:]
    if action=='--dis' and len(sys.argv)==4:
        run_display(sys.argv[2],sys.argv[3])

    elif action=='--op' and len(sys.argv)==5:
        if sys.argv[3]==sys.argv[4]:
            print("     Input flight path file name and output file name  should be different!")
            print("     If you continue with same name, You couldn't be able to run \"Test\" later")
            is_same_name = raw_input("     Do you want to continue? (Y/N):")
            if is_same_name.lower()[0]=='y':
                run_flight_optimization(sys.argv[2],sys.argv[3],sys.argv[4])
        else:
            run_flight_optimization(sys.argv[2], sys.argv[3], sys.argv[4])
    elif action=='--test' and len(sys.argv)==4:
        Test.test_optimization(sys.argv[2],sys.argv[3])

    else:
        print_log()

else:
    print_log()



