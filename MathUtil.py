from math import acos
from math import sqrt
from math import pi

def length(v):
    """
    This function calculates the length of a given vector.

    @param v: Vector representation of a 2-d coordinates
    @Return: Returns the length of the vector.
    """
    return sqrt(v[0]**2+v[1]**2)

def dot_product(v,w):
    """
    This function calculate the dot product of two vector v and w.

    @param v: Vector representation of a 2-d coordinates.
    @param w: Vector representation of a 2-d coordinates.
    @Return: Return the dot product of v and w.
    """
    return v[0]*w[0]+v[1]*w[1]

def determinant(v,w):
    """
    This function calculate the determinant of two vector v and w.

    @param v: Vector representation of a 2-d coordinates.
    @param w: Vector representation of a 2-d coordinates.
    @Return: Return the determinant of v and w.
    """
    return v[0]*w[1]-v[1]*w[0]
def inner_angle(v,w):
    """
    This function calculate the inner angle  between v and w.

    @param v: Vector representation of a 2-d coordinates.
    @param w: Vector representation of a 2-d coordinates.
    @Return: Return the inner angle of v and w.
    """
    cosx=dot_product(v,w)/(length(v)*length(w))
    rad=acos(cosx) # in radians
    return rad*180/pi # returns degrees

def angle_anti_clockwise(A, B):
    """
    Calculate the anti clock-wise angle between A and B.

    @param A: Given 2-d coordinate.
    @param B: Given 2-d coordinate.
    @Return: Return the anti-clockwise angle between A and B.
    """
    inner=inner_angle(A,B)
    det = determinant(A,B)
    if det<0: #this is a property of the det. If the det < 0 then B is clockwise of A
        return 360-inner
    else: # if the det > 0 then A is immediately clockwise of B
        return inner

def distance_a_to_b(point_A, point_B):
    """
     Calculate the distance between A and B.
    @param A: Given 2-d coordinate.
    @param B: Given 2-d coordinate.
    @Return: Return the distance between A and B.
    """
    difference_of_x = (point_A[0] - point_B[0])
    difference_of_y = (point_A[1] - point_B[1])
    return sqrt(difference_of_x ** 2+ difference_of_y ** 2)