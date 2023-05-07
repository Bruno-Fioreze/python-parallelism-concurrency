import multiprocessing

def square(number):
    return number ** 2

if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print(results)