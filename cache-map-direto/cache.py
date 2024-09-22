from typing import override, Optional
from memory import MemoryInterface
from lib import check_valid_address

class _CacheLine:
    def __init__(self, k: int, tag: int) -> None:
        self._tag = tag
        self.modified = False
        self._data = [0] * k  # k palavras

    def get(self) -> dict:
        return {
            'tag': self._tag,
            'modified': self.modified,
            'data': self._data,
        }

    def set(self, address: int, value: int) -> None:
        self._data[address] = value
        self.modified = True

class Cache(MemoryInterface):
    def __init__(self, kcs: int, kcls: int, ram: MemoryInterface) -> None:
        self._kcs = kcs
        self._ram = ram
        self._kcls = kcls
        self._cache_size = 2 ** kcs #m blocos
        self._cache_line_size = 2 ** kcls #k palavras
        self._lines = [
            _CacheLine(self._cache_line_size, tag) for tag in range(self._cache_size)
        ]

    def getk(self) -> tuple: return self._kcs, self._kcls

    def print_cache_lines(self):
        for line in self._lines: print(line.get())

    @override
    def capacity(self) -> int: return self._cache_size

    @override
    def _valid_address(self, address: int) -> None:
        check_valid_address(self._cache_size, address)

    @override
    def read(self, address: int) -> int:
        self._valid_address(address)
        r = (address // self._cache_line_size) % self._cache_size
        t = address // (self._cache_size * self._cache_line_size)
        cache_line = self._lines[r]
        if cache_line.get()['tag'] == t:
            print(f"Cache hit! Endereço {address}")
            w = address % self._cache_line_size
            return cache_line.get()['data'][w]
        else:
            print(f"Cache miss! Endereço {address}")
            self.write(address, None)
            return self.read(address)

    @override
    def write(self, address: int, value: Optional[int]) -> None:
        self._valid_address(address)
        r = (address // self._cache_line_size) % self._cache_size
        t = address // (self._cache_size * self._cache_line_size)
        cache_line = self._lines[r]
        if cache_line.modified:
            start_addr = (cache_line.get()['tag'] * self._cache_size + r) * self._cache_line_size
            for i in range(self._cache_line_size):
                self._ram.write(start_addr + i, cache_line.get()['data'][i])
        start_addr = (t * self._cache_size + r) * self._cache_line_size
        cache_line.get()['tag'] = t
        for i in range(self._cache_line_size):
            cache_line.get()['data'][i] = self._ram.read(start_addr + i)
        cache_line.modified = False
