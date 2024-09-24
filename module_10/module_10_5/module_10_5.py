import multiprocessing
from datetime import datetime


def read_info(name):
    with open(name, "r") as file:
        all_data = file.readlines()
    return all_data


# filenames = [f"./Homeworks/module_10/module_10_5/file {n}.txt" for n in range(1, 5)]
filenames = [f"./file {n}.txt" for n in range(1, 9)]


if __name__ == "__main__":
    # for n in range(1, 9):
    #     with open(f"./file {n}.txt", "w") as f:
    #         for i in range(10_000_000):  # Пример большого количества строк
    #             f.write(f"This is line {i} in file {n}\n")

    start = datetime.now()

    for file in filenames:
        read_info(file)

    end = datetime.now()
    print("Without multiprocessing: ", end - start)

    start_2 = datetime.now()

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.map(read_info, filenames)

    end_2 = datetime.now()
    print("With multiprocessing: ", end_2 - start_2)
