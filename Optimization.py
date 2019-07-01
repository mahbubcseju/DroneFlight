
import  MathUtil
class Optimization:
    def __init__(self, sweep_points, flight_points):
        """
        Constructor of DisplayUtil class.

        @param sweep_points: A list of angle and distance of all sweep.
        @param flight_points: A list of the flight points.
        """
        self.sweep_points = sweep_points
        self.flight_points = flight_points

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



    def is_possible_a_to_b(self,boundary_point, point_a, point_b):

        """
        This function checks whether it is possible to go from point_a to point_b by
        straight line. It first calculate the angle between point_a and point_b, then
        checks the boundary_point  for that angle and also check the boundary for that
        angle. If the boundary distance is greater then the distance between point_a
        and point_b then it is considered that we can go straightly from point_a to
        point_b.

        @param boundary_point: Boundary point of a sweep calculated using given data.
        @param point_a: Current position of drone/lidar.
        @param point_b: Next position of drone/lidar.
        @Return: return 1 if there is no obstacle from point point_a to point_b when it is
                 considered as straight line otherwise return 0
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
         Traverse through the path. When  I am  at position of index i,
         I tried to find whether is there any way to  go at position of
         index j (all j such that j>i) by straight line. For each i, we
         check continuously up to the last ending position. When I find any
         position of index j which is not reachable from position  of index
         i, I don't check for the rest position after j. If position of index
         j is not reachable by straight line, then I consider that position
         of index (j+1) is not reachable by straight line. After position of
         index i, I directly go to position of index position of index j as
         position of index j is reachable from position of index  i. So I just
         ommit all the position between index i and j. After that I update  i
         using j. I insert the position of each i in a list and finally return
         that list.

         @Return: returns optimized  flightPath.

        """
        optimized_sweep_points = []
        optimized_flight_points = []
        current_sweep = 0
        while current_sweep < len(self.flight_points):
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
