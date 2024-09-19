# Primeira etapa: corrigir o código da cache e adicionar a implementação da RAM.

# Corrigindo o arquivo cache.py e completando a lógica de "cache miss", dirty bit, e carregamento de dados.
class CacheLine:
    def __init__(self, size):
        self.tag = None  # Etiqueta para o bloco de memória
        self.data = [0] * size  # Dados armazenados na cache line
        self.dirty = False  # Flag para indicar se a linha foi modificada

class Cache:
    def __init__(self, cache_size, line_size, ram):
        self.cache_size = 2 ** cache_size  # Tamanho total da cache
        self.line_size = 2 ** line_size  # Tamanho de cada cache line
        self.lines = [CacheLine(self.line_size) for _ in range(self.cache_size)]  # Inicializando as cache lines
        self.ram = ram  # Referência à memória RAM

    def access(self, address):
        r = (address // self.line_size) % self.cache_size  # Calcula o índice do cache line
        t = address // (self.cache_size * self.line_size)  # Calcula a tag

        cache_line = self.lines[r]
        if cache_line.tag == t:  # Cache hit
            w = address % self.line_size  # Offset dentro da cache line
            return cache_line.data[w]
        else:  # Cache miss
            print(f"Cache miss! Endereço {address}")  # Imprimir cache miss
            self.load_from_ram(address)  # Carregar o bloco correspondente da RAM para a cache
            return self.access(address)  # Recursivamente acessar a cache após o carregamento

    def load_from_ram(self, address):
        r = (address // self.line_size) % self.cache_size  # Índice da cache line
        t = address // (self.cache_size * self.line_size)  # Calcula a tag correspondente

        cache_line = self.lines[r]

        # Se a cache line foi modificada, gravar de volta na RAM
        if cache_line.dirty:
            start_addr = (cache_line.tag * self.cache_size + r) * self.line_size
            for i in range(self.line_size):
                self.ram.write(start_addr + i, cache_line.data[i])

        # Carregar novo bloco da RAM para a cache
        start_addr = (t * self.cache_size + r) * self.line_size
        cache_line.tag = t
        for i in range(self.line_size):
            cache_line.data[i] = self.ram.read(start_addr + i)

        # Marcar a linha de cache como não modificada (clean)
        cache_line.dirty = False


# Implementando a classe RAM herdando de MemoryInterface
class RAM:
    def __init__(self, address_bits):
        self.size = 2 ** address_bits  # Capacidade da RAM em palavras
        self.memory = [0] * self.size  # Inicializando a memória RAM com 0s

    def capacity(self):
        return self.size

    def _valid_address(self, address):
        if address < 0 or address >= self.size:
            raise EnderecoInvalido(address)

    def read(self, address):
        self._valid_address(address)
        return self.memory[address]

    def write(self, address, value):
        self._valid_address(address)
        self.memory[address] = value


# Classe de exceção para endereços inválidos
class EnderecoInvalido(Exception):
    def __init__(self, address):
        self.ender = address
        super().__init__(f"Endereço inválido: {address}")


# Testando com o exemplo principal fornecido no enunciado
try:
    ram = RAM(12)  # 4K de RAM (2**12)
    cache = Cache(7, 4, ram)  # total cache = 128 (2**7), cacheline = 16 (2**4)

    # Escrevendo valores na RAM
    inicio = 0
    ram.write(inicio, 110)
    ram.write(inicio + 1, 130)

    # Acessando os dados pela CPU (simulada)
    print("Valor na cache após execução:", cache.access(inicio))  # Deve gerar cache miss, carregar da RAM e retornar 110
    print("Valor na cache após execução:", cache.access(inicio + 1))  # Deve gerar cache miss, carregar da RAM e retornar 130

except EnderecoInvalido as e:
    print("Endereço inválido:", e.ender)  # Tratamento de exceção para endereços inválidos
