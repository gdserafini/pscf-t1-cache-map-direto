from typing import Optional, override
from lib import check_valid_address
from memory import MemoryInterface

class _RamWord:
    def  __init__(self, address: int, word):
        self._address = address
        self._word = word

    def get(self):
        return {
            'address': self._address,
            'word': self._word
        }

class Ram(MemoryInterface):
    """
    Memória Ram a ser utilizada para armazenamento de W = 2 ** k palavras.
    Cria uma lista privada de palavras self._words.
    :param k: Número de bits para representação dos endereços de memória: int
    """
    def __init__(self, k: int) -> None:
        self._k = k
        self._size = 2 ** k
        self._words = [_RamWord(address, 0) for address in range(self._size)]

    def print(self) -> None:
        for word in self._words:
            print(word.get())

    def getk(self) -> int: return self._k

    @override
    def read(self, address: int) -> Optional[dict]:
        """
        Retorna uma palavra da memória conforme endereço específicado
        :param address: Endereço a ser lido: int
        :return: Palavra: int
        """
        self._valid_address(address)
        return self._words[address].get()

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
        self._valid_address(address)
        data = _RamWord(address, value)
        self._words[address] = data

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
