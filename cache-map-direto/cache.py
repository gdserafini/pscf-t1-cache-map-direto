from memory import MemoryInterface

class Cache(MemoryInterface):
    #TODO -> com mapeamento direto

    # def __init__(self, k: int, ram: RAM):
    #     Memory_Interface.__init__(self, ram.capacity())
    #     self.cache_size = 2 ** k
    #     self.ram = ram
    #     self.data = [0] * self.cache_size
    #     self.block = -1
    #     self.modified = False
    #
    #
    # @override
    # def capacity(self) -> int: pass
    #
    # @override
    # def _valid_address(self, address: int) -> None: pass
    #
    # @override
    # def read(self, address: int) -> int:
    #     if self.cache_hit(address):
    #         print("Cache HIT:", address)
    #     else:
    #         print("Cache MISS:", address)
    #         block_address = int(address / self.cache_size)
    #         if self.modified:
    #             for i in range(self.cache_size):
    #                 self.ram.write(self.block * self.cache_size + i, self.data[i])
    #         for i in range(self.cache_size):
    #             self.data[i] = self.ram.read(block_address * self.cache_size + i)
    #         self.block = block_address
    #         self.modified = False
    #     return self.data[address % self.cache_size]
    #
    # @override
    # def write(self, address: int, value: int) -> None:
    #     if self._cache_hit(address):
    #         print("Cache HIT:", address)
    #     else:
    #         print("Cache MISS:", address)
    #         block_address = int(address / self.cache_size)
    #         if self.modified:
    #             for i in range(self.cache_size):
    #                 self.ram.write(self.block * self.cache_size + i, self.data[i])
    #         for i in range(self.cache_size):
    #             self.data[i] = self.ram.read(block_address * self.cache_size + i)
    #         self.block = block_address
    #         self.modified = False
    #     self.data[address % self.cache_size] = value
    #     self.modified = True
    #
    # def _cache_hit(self, address: int) -> bool:
    #     block_address = int(address / self.cache_size)
    #     return block_address == self.block
    pass