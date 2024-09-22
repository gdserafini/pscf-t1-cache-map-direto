from io_class import IO
from ram import Ram
from cache import Cache, _CacheLine
from cpu import CPU

# class Machine:
#     def __init__(self, cpu, io, ram, cache):
#         self.cpu = cpu
#         self.io = io
#         self.ram = ram
#         self.cache = cache
#
#     def run(self, data: list[int]) -> None:
#         while self.cpu.run(len(data)):
#             address = self.cpu.getpc()
#             w, s, t, r = self._getwstr(address)
#             cache_line: _CacheLine = self.cache.read(w)
#             if r == cache_line.get()['tag']:
#                 self.io.input(f'Cache hit: {r}')
#                 self.io.output()
#             else:
#                 self.io.input(f'Cache miss: {r}')
#                 self.io.output()
#
#     def _getwstr(self, address: int) -> tuple:
#         kcs, kcls = self.cache.getk()
#         w = kcls
#         r = kcs
#         x = self.ram.getk()
#         t = x - r - x
#         s = t + r
#         return w, s, t, r

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
