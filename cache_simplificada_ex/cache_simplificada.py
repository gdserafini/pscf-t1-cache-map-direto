import sys
from typing_extensions import override

class IO:
    def __init__(self, stdin: sys.stdin, stdout: sys.stdout):
        self.stdin = stdin
        self.stdout = stdout

    def output(self, string: str) -> None:
        print(string, end=' ')

    def input(self, prompt: str) -> str:
        return input(prompt)

class InvalidAddress(Exception):
    def __init__(self, address: int):
        self.address = address

class Memory_Interface:
    def __init__(self, size: int):
        self.size = size

    def capacity(self) -> int:
        return self.size

    def check_address(self, address: int) -> None:
        if address < 0 or address >= self.size:
            raise InvalidAddress(address)

    def read(self, address: int) -> int: pass

    def write(self, address: int, value: int) -> None: pass

class RAM(Memory_Interface):
    def __init__(self, k: int):
        Memory_Interface.__init__(self, 2**k)
        self.size = 2 ** k
        self.words = [0] * self.size

    @override
    def read(self, address: int) -> int:
        self.check_address(address)
        return self.words[address]

    @override
    def write(self, address: int, word: int) -> None:
        self.check_address(address)
        self.words[address] = word

class CPU:
    def __init__(self, cache: Memory_Interface, io: IO):
        self.cache = cache
        self.io = io
        self.PC = 0
        self.A = self.B = self.C = 0

    def run(self, address: int) -> None:
        self.PC = address
        self.A = self.cache.read(self.PC)
        self.PC += 1
        self.B = self.cache.read(self.PC)
        self.PC += 1
        self.C = 1
        while self.A <= self.B:
            self.cache.write(self.A, self.C)
            self.io.output(f'{self.A} = {self.C}\n')
            self.C += 1
            self.A += 1

class Cache(Memory_Interface):
    def __init__(self, k: int, ram: RAM):
        Memory_Interface.__init__(self, ram.capacity())
        self.cache_size = 2 ** k
        self.ram = ram
        self.data = [0] * self.cache_size
        self.block = -1
        self.modified = False

    @override
    def read(self, address: int) -> int:
        if self.cache_hit(address):
            print("Cache HIT:", address)
        else:
            print("Cache MISS:", address)
            block_address = int(address / self.cache_size)
            if self.modified:
                for i in range(self.cache_size):
                    self.ram.write(self.block * self.cache_size + i, self.data[i])
            for i in range(self.cache_size):
                self.data[i] = self.ram.read(block_address * self.cache_size + i)
            self.block = block_address
            self.modified = False
        return self.data[address % self.cache_size]

    @override
    def write(self, address: int, value: int) -> None:
        if self.cache_hit(address):
            print("Cache HIT:", address)
        else:
            print("Cache MISS:", address)
            block_address = int(address / self.cache_size)
            if self.modified:
                for i in range(self.cache_size):
                    self.ram.write(self.block * self.cache_size + i, self.data[i])
            for i in range(self.cache_size):
                self.data[i] = self.ram.read(block_address * self.cache_size + i)
            self.block = block_address
            self.modified = False
        self.data[address % self.cache_size] = value
        self.modified = True

    def cache_hit(self, address: int) -> bool:
        block_address = int(address / self.cache_size)
        return block_address == self.block

def main() -> None:
    try:
        pass
    except InvalidAddress as e:
        print('Endereço inválido: ', e.address, file=sys.stderr)

if __name__ == '__main__':
    main()
