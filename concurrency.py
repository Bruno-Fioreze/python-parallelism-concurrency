import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print(letter)

if __name__ == '__main__':
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()