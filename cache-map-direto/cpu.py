gfrom memory import MemoryInterface
from io_class import IO

class CPU:
    def __init__(self, cache: MemoryInterface, io: IO):
        self._cache = cache
        self._io = io
        self._PC = 0
        self._A = self._B = self._C = 0

    def run(self, address: int) -> None:
        self._write_regs(address)
        while self._A <= self._B:
            self._write_mem()

    def _write_regs(self, address: int) -> None:
        self._PC = address
        self._A = self._cache.read(self._PC)
        self._PC += 1
        self._B = self._cache.read(self._PC)
        self._PC += 1
        self._C = 1

    def _write_mem(self) -> None:
        self._cache.write(self._A, self._C)
        self._io.input(f'{self._A} = {self._C}\n')
        self._io.output()
        self._C += 1
        self._A += 1