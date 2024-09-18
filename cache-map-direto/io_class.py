from typing import Optional

class IO:
    """
    Sistema de I/O que será relacionado a um CPU para entrada e saída de dados.
    Recebe uma lista de kargs como uma lista de strings
    """
    _prompt: str

    def __init__(self, kargs: Optional[list[str]]) -> None:
        self._kargs = kargs

    def output(self) -> Optional[str]:
        """
        Retorna o valor de input
        :return: Valor de output: str
        """
        return self._prompt if self._prompt else None

    def input(self, prompt: str) -> None:
        """
        Insere um valor de prompt com input, a ser exibido como output
        :param prompt: Input prompt: str
        :return: None
        """
        if type(prompt) != str:
            raise TypeError(prompt)
        self._prompt = prompt

    def get_kargs(self) -> Optional[list[str]]:
        """
        Retorna os kargs definidos na criação do objeto, sendo uma lista de strings
        :return: Lista de kargs ou None: str
        """
        return self._kargs if len(self._kargs) > 0 else None