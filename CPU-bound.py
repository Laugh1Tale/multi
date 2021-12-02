import concurrent.futures
from hashlib import md5
from random import choice


def generate_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()
        if h.endswith("00000"):
            print(s, h)


def async_generate_coins(workers_number):
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers_number) as executor:
        executor.map(generate_coin())


if __name__ == '__main__':
    # generate_coin()
    async_generate_coins(5)
