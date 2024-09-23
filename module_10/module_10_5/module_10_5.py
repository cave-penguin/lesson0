import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()
    return all_data


filenames = [f"./file {n}.txt" for n in range(1, 5)]


if __name__ == "__main__":
    start = datetime.now()

    for file in filenames:
        read_info(file)

    end = datetime.now()
    print("Without multiprocessing: ", end - start)

    start_2 = datetime.now()
    
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, filenames)
        
    end_2 = datetime.now()
    print("With multiprocessing: ", end_2 - start_2)
