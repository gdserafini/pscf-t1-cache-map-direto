class RAM:
    def __init__(self, bits):
        self.size = 2 ** bits  # Tamanho da RAM, ex: 2^12 = 4096 palavras
        self.memory = [0] * self.size  # Inicializando a RAM com 0s

    def read(self, address):
        if address < 0 or address >= self.size:
            raise EnderecoInvalido(address)
        return self.memory[address]

    def write(self, address, value):
        if address < 0 or address >= self.size:
            raise EnderecoInvalido(address)
        self.memory[address] = value

class EnderecoInvalido(Exception):
    def __init__(self, ender):
        self.ender = ender
        super().__init__(f"Endereço inválido: {ender}")