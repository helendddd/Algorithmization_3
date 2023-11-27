import time


def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1


array_lengths = list(range(0, 1000, 100))
value_worst = -1

for length in array_lengths:
    array_to_search = list(range(length))
    value_average = length // 2

    # Худший случай
    start_time_worst = time.time()
    linear_search(array_to_search, value_worst)
    end_time_worst = time.time()
    exe_time_worst = end_time_worst - start_time_worst

    # Средний случай
    start_time_average = time.time()
    linear_search(array_to_search, value_average)
    end_time_average = time.time()
    exe_time_average = end_time_average - start_time_average
    print(f"Время выполнения худшего случая: {exe_time_worst} сек.")
    print(f"Время выполнения среднего случая: {exe_time_average} сек.\n")
