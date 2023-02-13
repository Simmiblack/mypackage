from mypackage import myModule

def test_sq_cube():
    '''this should be used to test my function sq_cube
    
    '''
    assert myModule.sq_cube([1,2,3,4,6]) == [[4, 8], [16, 64], [36, 216]], 'incorrect'
    assert myModule.sq_cube([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]) == [[4, 8], [16, 64], [36, 216], [64, 512], [100, 1000]], 'incorrect'
    assert myModule.sq_cube([9.80665, 3.141, 1.618033988, 2.41421562]) == [[100, 1000], [4, 8], [4, 8]], 'incorrect'
    assert myModule.sq_cube([50/2, 40/3, 30/4, 20/5, 10/6]) == [[64, 512], [16, 64], [4, 8]], 'incorrect'