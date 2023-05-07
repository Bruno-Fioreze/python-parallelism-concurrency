import threading, requests as rq
from pprint import pprint

URL = "https://pokeapi.co/api/v2/pokemon"


def detail_by_id(numbers, number_thread):
    pokes = []
    for number in numbers:
        r = rq.get(f"{URL}/{number}")
        data = r.json()
        data = {"name": data["name"], "status_code": r.status_code, "id": number}
        pokes.append(data)
        print(f"Thread: {number_thread} / data: {data}")
    return pokes


if __name__ == "__main__":
    threads, poke_ids = [], range(1, 151)
    slice, initial, final = 25, 0, 0

    for thread in range(0, 6):
        if thread:
            initial = initial + slice
        final = final + slice
        arg = [poke_ids[initial:final], thread]

        thread = threading.Thread(target=detail_by_id, args=(arg))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
