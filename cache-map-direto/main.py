from io_class import IO
from ram import Ram
from cache import Cache
from cpu import CPU

def main() -> None:
    #TODO -> com base no script definido no trabalho t1

    # try:
    #     io = IO(None)
    #     ram = Ram(12)  # 4K de RAM (2**12)
    #     cache = Cache(7, 4, ram)  # total cache = 128 (2**7), cacheline = 16 (2**4)
    #     cpu = CPU(cache, io)
    #     START = 0
    #     ram.write(START, 110)
    #     ram.write(START + 1, 130)
    #     cpu.run(START)
    # except ValueError as ve:
    #     print(ve)
    pass

if __name__ == '__main__':
    main()
