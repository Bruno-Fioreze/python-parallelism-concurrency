import multiprocessing, requests as rq, psutil
from pprint import pprint

URL = "https://pokeapi.co/api/v2/pokemon"


def detail_by_id(number):
    core_number = psutil.Process().cpu_num()
    r = rq.get(f"{URL}/{number}")
    data = r.json()
    data = {
        "name": data["name"],
        "status_code": r.status_code,
        "id": number,
        "core_number": core_number,
    }
    pprint(data)
    return data


if __name__ == "__main__":

    numbers = range(1, 151)
    with multiprocessing.Pool(processes=12) as pool:
        results = pool.map(detail_by_id, numbers)
