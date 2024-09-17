def check_valid_address(size: int, address: int) -> bool:
    """
    Verifica se um valor de endereço é valido.
    Lança exceção InvalidTypeError caso parâmetros não sejam números inteiros.
    :param size: Tamanho da memória: int
    :param address: Endereço a ser verificado: int
    :return: Se endereço é valido: bool
    """
    if type(address) != int or type(size) != int:
        raise TypeError(
            f"'{address if type(address) != int else size}' must be an integer"
        )
    return 0 < address < size
