def sum_of_array(arr1, arr2):
    """두 행렬의 덧셈을 구하라.

    시간 복잡도:
    arr1가 M x N 크기의 행렬이라고 할 떄 O(NM)
    """
    return [sum_of_rows_in_arrays(arr1[row], arr2[row]) for row in range(len(arr1))]


def sum_of_rows_in_arrays(row1, row2):
    return [row1[row] + row2[row] for row in range(len(row1))]


def test_sum_of_array():
    assert sum_of_array([[1, 2],
                         [2, 3]],
                        [[3, 4],
                         [5, 6]]) == [[4, 6],
                                      [7, 9]]
    assert sum_of_array([[1], [2]],
                        [[3], [4]]) == [[4], [6]]

def test_sum_of_rows_in_arrays():
    assert sum_of_rows_in_arrays([1, 2], [3, 4]) == [4, 6]
    assert sum_of_rows_in_arrays([1], [3]) == [4]
