from CsvHelper import CsvHelper
from DisplayUtil import DisplayUtil
from Optimization import Optimization
csv_helper=CsvHelper("points.csv","path.csv")
flight_path=csv_helper.read_flight_path_element()
if len(flight_path)!=34:
    print("Number of sweep is not 34!Please check ! May be wrong flight path file included")
else:
    for point in range(len(flight_path)):
        print(flight_path[point][0],flight_path[point][1])

lidar_points=csv_helper.read_lidar_element()
if len(lidar_points)!=34:
    print("Number of sweep is not 34!Please check ! May be wrong lidar points file included")
else:
    for length in range(len(lidar_points)):
        print(length,len(lidar_points[length]))
optimization=Optimization(lidar_points,flight_path)
optimized_lidar_points,optimized_flight_path=optimization.optimization()
display_helper=DisplayUtil(optimized_lidar_points,optimized_flight_path)
display_helper.display_sweep()

