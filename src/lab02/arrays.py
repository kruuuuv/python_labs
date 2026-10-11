def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("пустой список")

    return (min(nums), max(nums))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unums = []
    for num in nums:
        if num not in unums:
            unums.append(num)
    unums.sort()
    return unums


def flatten(mat: list[list | tuple]) -> list:
    truenums = []
    for element in mat:
        if not isinstance(element, (list, tuple)):
            raise TypeError(f"элемент {element} не является списком или кортежем")
        truenums.extend(element)
    return truenums


print("min/max: ")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([-7, -1, -2, 3.4, 23, -2, -9.2]))
# print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print("sort: ")
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
print(unique_sorted([-3.34, 1, 5.5, -2.5, 1, -2, 0]))

print("flatten:")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1], (5, -2), [], [2, 4]]))
# print(flatten([[1, 2], "ab"]))


# a = int(input("if you need min_max - click '1', unique_sorted - click '2', or flatten - click '3'"))
# nums = []

# while True:
#     n = input()
#     if n == 'стоп':
#         break
#     nums.append(n)
