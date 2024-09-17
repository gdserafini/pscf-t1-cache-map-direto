class MemoryInterface:
    def capacity(self) -> int: pass
    def valid_address(self, address: int) -> bool: pass
    def read(self, address: int) -> int: pass
    def write(self, address: int, value: int) -> None: pass
