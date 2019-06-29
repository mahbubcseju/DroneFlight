from CsvHelper import CsvHelper
csv_helper=CsvHelper("points.csv","path.csv")
path=csv_helper.read_flight_path_element()
if len(path)!=34:
    print("Number of sweep is not 34!Please check ! May be wrong flight path file included")
else:
    for point in range(len(path)):
        print(path[point][0],path[point][1])

points=csv_helper.read_lidar_element()
if len(points)!=34:
    print("Number of sweep is not 34!Please check ! May be wrong lidar points file included")
else:
    for length in range(len(points)):
        print(length,len(points[length]))
