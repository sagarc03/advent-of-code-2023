def extrapolate(arr: list[int]) -> int:
    result: list[int] = []
    for i in range(len(arr) - 1):
        result.append(arr[i + 1] - arr[i])
    if all(x == 0 for x in result):
        return arr[-1]
    return arr[-1] + extrapolate(result)


def extrapolate_backwords(arr: list[int]) -> int:
    result: list[int] = []
    for i in range(len(arr) - 1):
        result.append(arr[i + 1] - arr[i])
    if all(x == 0 for x in result):
        return arr[0]
    return arr[0] - extrapolate_backwords(result)
