def find_smallest(arr: list[float], choice: str) -> tuple[float, int]:
    """Return smallest number and its index."""
    min_index: int = 0
    min: float = arr[0]
    length: int = len(arr)
    for item in range(length):
        if choice == "asc":
            if arr[item] < min:
                min = arr[item]
                min_index = item
        elif choice == "desc":
            if arr[item] > min:
                min = arr[item]
                min_index = item
    return min, min_index


def dumbsort(arr: list[float], choice: str) -> list[float]:
    """This is dumbsort, a cursed piece of code that shall not be ran on
    any machine.

    It:

    - Appends the original array to a new array as many times as there are items in the array
    - Iterates through each item of new_arr - those are the copies of the original sub_array
    - If the current sub array contains previously found smallest items, then remove them
    - Finds the smallest item in each sub array and removes any other items
    - Appends the newly found smallest item to a new list
    """

    length1 = len(arr)

    if length1 == 0:
        return []

    new_arr = []
    for item in range(length1):
        new_arr.append(arr[:])

    mins = []
    for i in range(length1):
        sub_array = new_arr[i]
        # print(sub_array, mins)

        length2 = len(mins)
        if length2 != 0:
            for k in range(length2):
                sub_array.remove(mins[k])

        length3 = len(sub_array)
        smallest = find_smallest(sub_array, choice)
        smallest_item = smallest[0]
        smallest_index = smallest[1]

        for right_pointer in range(length3 - 1, smallest_index, -1):
            del sub_array[right_pointer]
        for left_pointer in range(smallest_index - 1, -1, -1):
            del sub_array[left_pointer]

        mins.append(sub_array[0])
    return mins


def main():
    array: list[float] = [8.9, 72.3, 1.2, 1.2, 0.3, 4.2, 3.8, 3.2]
    # array: list[float] = []
    # array: list[float] = [13.2, 1.2, 82, 5.6, 8.054]
    # array: list[float] = [8.83076591550493, 7.29588656402785, 9.095076399130058, 12.460853135075789, 13.550548118185947, 8.308303888614308, 1.2582104427424756, 12.660184652741892, 1.8268792285831106, 9.552934319419952, 12.202705479042391, 0.5394433375732977, 1.2421279373947507, 5.412638044802769, 9.196125475637867, 9.781817982088901, 17.153249562561626, 14.004705567809483, 10.882392672303805, 5.729119852183036, 1.4025332370418497, 14.846741229622046, 1.5132164309736869, 4.983662568459627, 16.48516437484967, 10.838006586473808, 4.448730688948651, 15.986029405639998, 9.643062634560774, 1.4789562384751251, 1.9979165699662305, 11.134349875097033, 1.1179218695515545, 6.768735655628199, 2.060902072780284, 6.6011876716267315, 12.430782397125615, 6.177304286488885, 2.4226922323418916, 10.342181373594373, 4.367104951769333, 8.511601721000796, 5.261172659340457, 5.778101942701079, 5.824926763852936, 9.197578691952225, 4.870023869201534, 10.084389546559708, 0.7701718603723097, 4.095320438928384, 12.24587441171992, 16.131801005324043, 1.5709766621745647, 3.005708744276534]
    # array: list[float] = [12, 43, 36, 29]
    a = dumbsort(array, "asc")  # choose between asc and desc
    print(a)


if __name__ == "__main__":
    main()
