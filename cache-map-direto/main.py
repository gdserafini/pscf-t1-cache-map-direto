from io_class import IO
from ram import Ram
from cache import Cache
from cpu import CPU

def main() -> None:
    try:
         io = IO(None)
         ram = Ram(12)
         cache = Cache(7, 4, ram)
         cpu = CPU(cache, io)
         START = 0
         ram.write(START, 110)
         ram.write(START + 1, 130)
         cpu.run(START)
     except ValueError as ve:
         print(ve)

if __name__ == '__main__':
    main()
