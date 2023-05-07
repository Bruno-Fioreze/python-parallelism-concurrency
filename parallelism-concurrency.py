import multiprocessing
import threading


def square(number):
    return number**2


def print_numbers():
    for i in range(1, 6):
        print(i)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    t = threading.Thread(target=print_numbers)
    t.start()
    print(results)
    t.join()
