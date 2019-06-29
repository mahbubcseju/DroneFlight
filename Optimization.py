
import  MathUtil
class Optimization:
    def __init__(self, sweep_points, flight_points):
        """
        @param sweep_points: angle and distance of each sweep
        @param flight_points: Collection of the flight points

        Constructor of DisplayUtil class
        """
        self.sweep_points = sweep_points
        self.flight_points = flight_points

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



    def is_possible_a_to_b(self,boundary_point, point_a, point_b):

        """
        @param boundary_point: Boundary point of a sweep calculated using given data
        @param point_a: Current position of drone
        @param point_b: Next position of drone

        @Return: return 1 if there is no obstacle from point point_a to point_b when it is considered as straight line
                 otherwise return 0
        """
        angle= MathUtil.angle_anti_clockwise(point_a, point_b)
        # print(angle)
        temp_boundary_point = boundary_point[:]
        precision = 360.0 / len(temp_boundary_point)

        distance_between_point = MathUtil.distance_a_to_b(point_a, point_b)*1000
        #print(angle, 'log', dis, precision)
        for point in range(len(temp_boundary_point)):
            #print(temp_boundary_point[i][0], angle, temp_boundary_point[i][1], dis)
            if precision > abs(temp_boundary_point[point][0] - angle) and distance_between_point > temp_boundary_point[point][1]:
                return 0
        return 1

    def optimization(self):

        """
        @Return: returns optimized  flightPath and for each sweep of that
        flight path coordinates return LIDARPoint

        finds a better flight path that will result in the shortest possible
        travel time but still goes through the existing rooms.
        """
        optimized_sweep_points = []
        optimized_flight_points = []
        current_sweep = 0
        while current_sweep < len(self.flight_points):
            print(current_sweep)
            optimized_flight_points.append(self.flight_points[current_sweep])
            optimized_sweep_points.append(self.sweep_points[current_sweep])
            next_sweep =current_sweep + 1
            for remaining_sweep in range(current_sweep + 1, len(self.flight_points)):
                if self.is_possible_a_to_b(self.sweep_points[current_sweep],self.flight_points[current_sweep], self.flight_points[remaining_sweep]) == 1:
                    next_sweep = remaining_sweep
                else:
                    break
            current_sweep=next_sweep

        return optimized_sweep_points,optimized_flight_points
