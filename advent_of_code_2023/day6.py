def number_of_ways_to_beat(t: int, d: int, start: int = 0) -> int:
    result = 0
    for i in range(start, t + 1):
        if i * (t - i) > d:
            result += 1
    return result


def first_time(start: int, end: int, total_time: int, duration: int) -> int:
    mid = -1
    while start <= end:
        mid = start + (end - start) // 2
        if mid == 0 or (
            duration >= (mid - 1) * (total_time - (mid - 1))
            and duration < mid * (total_time - mid)
        ):
            return mid
        if duration > mid * (total_time - mid):
            start = mid + 1
        else:
            end = mid - 1
    return mid


def last_time(start: int, end: int, total_time: int, duration: int) -> int:
    mid = -1
    while start <= end:
        mid = start + (end - start) // 2
        if mid == end or (
            duration >= (mid + 1) * (total_time - (mid + 1))
            and duration < mid * (total_time - mid)
        ):
            return mid
        if duration < mid * (total_time - mid):
            start = mid + 1
        else:
            end = mid - 1
    return mid


def number_of_ways_to_beat_binary_search(t: int, d: int, start: int = 0) -> int:
    first_time_to_beat = first_time(start, t, t, d)
    last_time_to_beat = last_time(start, t, t, d)
    return last_time_to_beat - first_time_to_beat + 1
