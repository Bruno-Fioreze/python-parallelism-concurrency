import multiprocessing, requests as rq
from pprint import pprint

URL = "https://pokeapi.co/api/v2/pokemon"


def detail_by_id(number):
    r = rq.get(f"{URL}/{number}")
    data = r.json()
    data = {"name": data["name"], "status_code": r.status_code, "id": number}
    return data


if __name__ == "__main__":

    numbers = range(1, 151)
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(detail_by_id, numbers)
