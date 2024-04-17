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


def selection_sort(file_name, direction="ascending"):
    data = read_data(file_name)
    numbers = data["series_1"]
    list_2 = data["series_2"]
    list_3 = data["series_3"]

    for i in range(len(numbers)):

        min_idx = i
        for num_idx in range(i + 1,len(numbers)):
            if direction == "ascending":
                if numbers[min_idx] > numbers[num_idx]:
                    min_idx = num_idx
            elif direction == "descending":
                if numbers[min_idx] > numbers[num_idx]:
                    min_idx = num_idx
        numbers[i],numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers
def bubble_sort(file_name):
   data = read_data(file_name)
   seznam = data["series_1"]
   j = 0
   for k in range(j, len(seznam)-1):
        i = 0
        for idx in range(i, len(seznam)-k - 1):
            cur_num = seznam[idx]
            next_num = seznam[idx + 1]
            if cur_num > next_num:
                seznam[idx], seznam[idx + 1] = seznam[idx + 1], seznam[idx]
            i += 1
        j += 1
   return seznam




def main():
    seznam = bubble_sort("numbers.csv")
    print(seznam)
    pass


if __name__ == '__main__':
    main()
