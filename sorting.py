import csv
import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1":[], "series_2":[], "series_3": []}

        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [row[key]]
                else:
                    data[key].append(int(row[key]))

    return data


def selection_sort(file_name):
    data = read_data(file_name)
    numbers = data["series_1"]
    list_2 = data["series_2"]
    list_3 = data["series_3"]

    # for item in list_1:
    #     i = 1
    #     idx = list_1.index(item)
    #     num_of_cycles = len(list_1) - idx - 1
    #     while i <= num_of_cycles:
    #         if item > list_1[idx + i]:
    #             cur_idx = list_1.index(item)
    #         i += 1
    #     list_1[cur_idx], list_1[cur_idx + i] = list_1[cur_idx + i], list_1[cur_idx]
    for i in range(len(numbers)):

        min_idx = i
        for num_idx in range(i + 1,len(numbers)):
            if numbers[min_idx] > numbers[num_idx]:
                min_idx = num_idx
        numbers[i],numbers[min_idx] = numbers[min_idx], numbers[i]



    return numbers





def main():
    list_1 = selection_sort("numbers.csv")
    print(list_1)
    pass


if __name__ == '__main__':
    main()
