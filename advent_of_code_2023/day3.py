def get_valid_numbers(string_mat: list[str]) -> list[int]:
    n = len(string_mat)
    m = len(string_mat[0])
    visited = set()
    isValid = lambda r, c: r >= 0 and r < n and c >= 0 and c < m
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    result = []

    for i in range(n):
        for j in range(m):
            if (
                not string_mat[i][j].isdigit()
                and string_mat[i][j] != "."
                and (i, j) not in visited
            ):
                visited.add((i, j))
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if (
                        isValid(ni, nj)
                        and (ni, nj) not in visited
                        and string_mat[ni][nj].isdigit()
                    ):
                        visited.add((ni, nj))

                        # get the start of that number
                        while isValid(ni, nj - 1) and string_mat[ni][nj - 1].isdigit():
                            nj -= 1
                        temp = 0
                        while isValid(ni, nj) and string_mat[ni][nj].isdigit():
                            visited.add((ni, nj))
                            temp = temp * 10 + int(string_mat[ni][nj])
                            nj += 1

                        result.append(temp)

    return result


def get_valid_gear_ratio(string_mat: list[str]) -> list[int]:
    n = len(string_mat)
    m = len(string_mat[0])
    visited = set()
    isValid = lambda r, c: r >= 0 and r < n and c >= 0 and c < m
    direction = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    result = []

    for i in range(n):
        for j in range(m):
            if string_mat[i][j] == "*" and (i, j) not in visited:
                visited.add((i, j))
                numbers_around_gear = []
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if (
                        isValid(ni, nj)
                        and (ni, nj) not in visited
                        and string_mat[ni][nj].isdigit()
                    ):
                        visited.add((ni, nj))
                        # get the start of that number
                        while isValid(ni, nj - 1) and string_mat[ni][nj - 1].isdigit():
                            nj -= 1
                        temp = 0
                        while isValid(ni, nj) and string_mat[ni][nj].isdigit():
                            visited.add((ni, nj))
                            temp = temp * 10 + int(string_mat[ni][nj])
                            nj += 1
                        numbers_around_gear.append(temp)
                if len(numbers_around_gear) == 2:
                    result.append(numbers_around_gear[0] * numbers_around_gear[1])

    return result
