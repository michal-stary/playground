def two_sum(xs, target_sum):
    """
    Return the two numbers in xs that sum to target_sum.
    
    >>> two_sum([2, 7, 11, 15], 9)
    [2, 7]
    >>> two_sum([3, 2, 4], 6)
    [2, 4]
    >>> two_sum([2, 7, 11, 15], 10)
    []
    """
    # sort xs in O(nlogn) time
    sorted_xs = sorted(xs)

    # iterate through xs
    i = 0
    for i in range(len(sorted_xs)):
        # binary search for target_sum - xs[i] where target index != i, (O(logn) time
        j = 0
        k = len(sorted_xs) - 1
        while j <= k:
            mid = (j + k) // 2
            if sorted_xs[mid] == target_sum - sorted_xs[i] and mid != i:
                return [sorted_xs[i], target_sum - sorted_xs[i]]
            elif sorted_xs[mid] < target_sum - sorted_xs[i]:
                j = mid + 1
            else:
                k = mid - 1 
    return []

def test_two_sum():
    """
    Tests the two_sum function.
    """

    assert two_sum([2, 7, 11, 15], 9) == [2, 7]
    assert two_sum([3, 2, 4], 6) == [2, 4]
    assert two_sum([2, 7, 11, 15], 10) == []
    assert two_sum([2, 7, 11, 15], 13) == [2, 11]
    assert two_sum([2, 7, 11, 15], 17) == [2, 15]
    assert two_sum([3, 5, -4, 8, 11, 1, -1, 6], 10) == [-1, 11]

    # test edge cases
    assert two_sum([], 0) == []
    assert two_sum([1], 0) == []
    assert two_sum([1], 1) == []
    assert two_sum([1, 2], 1) == []
    assert two_sum([1, 2], 4) == []
    assert two_sum([1, 2], 3) == [1, 2]
    assert two_sum([1, 2, 3], 3) == [1, 2]
    assert two_sum([1, 2, 3], 4) == [1, 3]
    assert two_sum([1, 2, 3], 5) == [2, 3]

    # target sum is negative
    assert two_sum([1, 2, 3], -1) == []
    assert two_sum([-1, -2, -3], -1) == []
    assert two_sum([-1, -2, -3], -2) == []
    assert two_sum([-1, -2, -3], -3) == [-2, -1]
    assert two_sum([1, -5, -3], -4) == [-5, 1]
    # target sum is zero
    assert two_sum([1, 2, 3], 0) == []
    assert two_sum([-1, -2, -3], 0) == []
    assert two_sum([0, 1, 2, 3], 0) == []
    assert two_sum([0, -1, -2, -3], 0) == []

    # target sum is positive
    assert two_sum([1, 2, 3], 1) == []
    assert two_sum([-1, -2, -3], 1) == []
    assert two_sum([1, 2, 3], 2) == []
    assert two_sum([-1, -2, -3], 2) == []
    assert two_sum([1, 2, 3], 3) == [1,2]
    assert two_sum([-1, -2, -3], 3) == []
    assert two_sum([1, 2, 3], 4) == [1, 3]

    # new test cases
    assert two_sum([10**18, 10**18-1], 2*10**18-1) == [10**18-1, 10**18]
    assert two_sum([-10**18, 10**18], 0) == [-10**18, 10**18]
    assert two_sum([0, 0], 0) == [0, 0]
    assert two_sum([0, 1, 2], 1) == [0, 1]
    assert two_sum([-1, -2, -3, -4], -7) == [-4, -3]
    assert two_sum([-5, -10, 5, 10], 0) == [-10, 10]
    assert two_sum([1, 2, 3, 4], 10) == []
    assert two_sum([-1, -2, -3, -4], -1) == []
    assert two_sum([5], 5) == []
    assert two_sum([1, 2, 3, 7], 8) == [1, 7]

    print("All tests passed.")


if __name__ == "__main__":
    test_two_sum()

