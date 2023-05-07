import multiprocessing, requests as rq
import threading
from pprint import pprint


URL = "https://pokeapi.co/api/v2/pokemon"


def detail_by_id(number):
    r = rq.get(f"{URL}/{number}")
    data = r.json()
    data = {"name": data["name"], "status_code": r.status_code, "id": number}
    return data


def another_function():
    print("another function")


if __name__ == "__main__":
    numbers = range(1, 10)
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(detail_by_id, numbers)

    t = threading.Thread(target=another_function)
    t.start()
    pprint(results)
    t.join()
