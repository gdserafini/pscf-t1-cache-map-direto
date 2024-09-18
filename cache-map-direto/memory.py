from typing import Optional

class MemoryInterface:
    """
    Interface para definição de memórias
    method capacity: Deve retornar o tamanho da memória com número inteiro
    method _valid_address: Deve lançar exceções de erros de endereço
    method read: Deve retornar uma palavra, caso exista, sendo um número inteiro
    method write: Deve salvar uma palavra em um endereço determinado, caso válido
    """
    def capacity(self) -> int: pass
    def _valid_address(self, address: int) -> None: pass
    def read(self, address: int) -> Optional[int]: pass
    def write(self, address: int, value: int) -> None: pass
