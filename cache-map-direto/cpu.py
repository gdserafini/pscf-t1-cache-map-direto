from memory import MemoryInterface
from io_class import IO

class CPU:
    """
    Classe de CPU responsável por executar um processo.
    Recebe os seguintes componetes de memória: cache, PC - e IO.
    Defini os registradores A,B e C como zero
    """
    def __init__(self, cache: MemoryInterface, io: IO):
        self._PC = -1
        self._A = self._B = self._C = 0
        self._cache = cache
        self._io = io

    def run(self, address: int) -> None:
        """
        Realiza a escrita na memória baseado nas definições de cache
        :param address: Endereço para escrita: int
        :return: None
        """
        self._write_regs(address)
        while self._A <= self._B:
            self._write_mem()

    def _write_regs(self, address: int) -> None:
        """
        Realiza a escrita temporária nos registradores
        :param address: Endereço para escrita: int
        :return: None
        """
        self._PC = address
        self._A = self._cache.read(self._PC)
        self._PC += 1
        self._B = self._cache.read(self._PC)
        self._PC += 1
        self._C = 1

    def _write_mem(self) -> None:
        """
        Realiza a escrita na memória baseada nas definições de regs e cache
        :return: None
        """
        self._cache.write(self._A, self._C)
        self._io.input(f'{self._A} = {self._C}\n')
        self._io.output()
        self._C += 1
        self._A += 1
