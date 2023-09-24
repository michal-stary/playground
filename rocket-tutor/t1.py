# import types
from typing import List

def square_array(x: List[int]) -> List[int]:
    """
    Squares each element of a list of integers and returns the result.
    Make sure it runs in O(n) time also for arrays with negative numbers.

    >>> square_array([1,2,3])
    [1, 4, 9]
    >>> square_array([2,4,6])
    [4, 16, 36]
    >>> square_array([-1,1,2])
    [1, 1, 4]
    """
    
    square_arr = [val**2 for val in x]

    # resort the new_arr in ascending order in O(n) time
    i = 0
    j = len(square_arr) - 1
    new_arr = []
    while i < j:
        if square_arr[i] > square_arr[j]:
            new_arr.append(square_arr[i])
            i += 1
        elif square_arr[i] <= square_arr[j]:
            new_arr.append(square_arr[j])
            j -= 1

    if i == j:
        new_arr.append(square_arr[i])
    
    square_arr = new_arr[::-1]

    return square_arr

# tests for square_array function
def test_square_array():
    """
    Tests the square_array function.    
    """

    assert square_array([1,2,3]) == [1,4,9]
    assert square_array([2,4,6]) == [4,16,36]
    assert square_array([0,1]) == [0,1]
    assert square_array([0]) == [0]
    assert square_array([-1,1,2]) == [1,1,4]
    assert square_array([-1,-2,-3]) == [1,4,9]
    assert square_array([-3,-2,-1]) == [1,4,9]
    assert square_array([-3,-2,-1,0,1,2,3]) == [0,1,1,4,4,9,9]
    assert square_array([-3,-2,-1,0,1,2,3,4]) == [0,1,1,4,4,9,9,16]
    assert square_array([-3,-2,-1,0,1,2,3,4,5]) == [0,1,1,4,4,9,9,16,25]
    assert square_array([-7, -5, -3, -1, 2, 4, 6]) == [1, 4, 9, 16, 25, 36, 49]
    
    print("All tests passed.")

if __name__ == "__main__":
    test_square_array()

    


