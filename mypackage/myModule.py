def sq_cube(numbers):
    ''' This function sq_cube returns a list of lists containing both the square and 
    the cube of only the even numbers in a given list. The function must also be able 
    to round the numbers to the nearest whole number
    e.g. [1 ,2, 4, 5, 6] yields [[2,8], [16,64], [36,216]]'''
    cube_square = [[round(i)**2, round(i)**3] for i in numbers if round(i) % 2 == 0]
    '''The above code is a list comprehension which tells python to returd a list of
    the squares and the cubes of a rounded integer i in the numbers that will be given 
    if the numbers are even'''
    return cube_square
