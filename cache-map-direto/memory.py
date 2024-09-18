from typing import Optional

class MemoryInterface:
    def capacity(self) -> int: pass
    def _valid_address(self, address: int) -> None: pass
    def read(self, address: int) -> Optional[int]: pass
    def write(self, address: int, value: int) -> None: pass
