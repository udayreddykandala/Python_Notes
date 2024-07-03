import pytest


def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 6) == -1


def test_binary_search_time():
    arr = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    start_time = time()
    result = binary_search(arr, target)
    end_time = time()
    elapsed_time = end_time - start_time
    assert result == 3
    print(f"Binary search time: {elapsed_time:.10f} seconds")


if __name__ == "__main__":
    pytest.main()
