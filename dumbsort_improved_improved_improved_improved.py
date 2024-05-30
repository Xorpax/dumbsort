def dumbsort(arr: list[float], choice: str="asc") -> list[float]:
    sorted_arr = []

    arr_len = len(arr)

    if arr_len == 0:
        return []

    new_arr = []
    # append n duplicates of arr to new_arr, where n is the number of elements in arr
    for item in range(arr_len):
        new_arr.append(arr[:])


    for i in range(arr_len):
        sub_array = new_arr[i]

        sorted_arr_len = len(sorted_arr)

        # remove min/max items found previously from the current sub_array
        if sorted_arr_len != 0:
            for item in sorted_arr:
                sub_array.remove(item)

        sub_array_len = len(sub_array)
        if choice == "asc":
            smallest_item = min(sub_array)
        elif choice == "desc":
            smallest_item = max(sub_array)
        smallest_index = sub_array.index(smallest_item)

        # remove items to the either side of the current min/max element
        for right_pointer in range(sub_array_len - 1, smallest_index, -1):
            del sub_array[right_pointer]
        for left_pointer in range(smallest_index - 1, -1, -1):
            del sub_array[left_pointer]

        sorted_arr.append(sub_array[0])
    return sorted_arr


def main():
    # array: list[float] = []  # edge case
    # array: list[float] = [8.9, 72.3, 1.2, 1.2, 0.3, 4.2, 3.8, 3.2]  # standard case 1
    # array: list[float] = [13.2, 1.2, 82, 5.6, 8.054]  # standard case 2
    array: list[float] = [8.83076591550493, 7.29588656402785, 9.095076399130058, 12.460853135075789, 13.550548118185947, 8.308303888614308, 1.2582104427424756, 12.660184652741892, 1.8268792285831106, 9.552934319419952, 12.202705479042391, 0.5394433375732977, 1.2421279373947507, 5.412638044802769, 9.196125475637867, 9.781817982088901, 17.153249562561626, 14.004705567809483, 10.882392672303805, 5.729119852183036, 1.4025332370418497, 14.846741229622046, 1.5132164309736869, 4.983662568459627, 16.48516437484967, 10.838006586473808, 4.448730688948651, 15.986029405639998, 9.643062634560774, 1.4789562384751251, 1.9979165699662305, 11.134349875097033, 1.1179218695515545, 6.768735655628199, 2.060902072780284, 6.6011876716267315, 12.430782397125615, 6.177304286488885, 2.4226922323418916, 10.342181373594373, 4.367104951769333, 8.511601721000796, 5.261172659340457, 5.778101942701079, 5.824926763852936, 9.197578691952225, 4.870023869201534, 10.084389546559708, 0.7701718603723097, 4.095320438928384, 12.24587441171992, 16.131801005324043, 1.5709766621745647, 3.005708744276534]  # standard case 3
    a = dumbsort(array)  # choose between asc and desc
    print(a)


if __name__ == "__main__":
    main()
