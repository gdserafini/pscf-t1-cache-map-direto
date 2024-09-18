from typing import override, Optional
from lib import check_valid_address
from memory import MemoryInterface

class Ram(MemoryInterface):
    """
    Memória Ram a ser utilizada para armazenamento de W = 2 ** k palavras.
    Cria uma lista privada de palavras self._words.
    :param k: Número de bits para representação dos endereços de memória: int
    """
    def __init__(self, k: int) -> None:
        self._size = 2 ** k
        self._words = [0] * self._size

    @override
    def read(self, address: int) -> Optional[int]:
        """
        Retorna uma palavra da memória conforme endereço específicado
        :param address: Endereço a ser lido: int
        :return: Palavra: int
        """
        if self._valid_address(address):
            return self._words[address]
        else: return None

    @override
    def write(self, address: int, value: int) -> None:
        """
        Escreve uma palavra em um endereço específico da memória Ram
        :param address: Endereço para escrita: int
        :param value: Palavra a ser escrita: int
        :return: None
        """
        if type(value) != int:
            raise TypeError("'value' must be an integer")
        if self._valid_address(address):
            self._words[address] = value
        else: return

    @override
    def capacity(self) -> int:
        """
        Retorna a capacidade total da Ram = 2 ** k
        :return: Capacidade: int
        """
        return self._size

    @override
    def _valid_address(self, address: int) -> None:
        """
        Verifica se um endereço de meméria na Ram é válido.
        :param address: Endereço a ser verificado: int
        :return: Válido/Inválido: bool
        """
        check_valid_address(self._size, address)
