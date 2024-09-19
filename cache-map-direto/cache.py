class CacheLine:
    def __init__(self, size):
        self.tag = None  
        self.data = [0] * size  
        self.dirty = False  

class Cache:
    def __init__(self, cache_size, line_size, ram):
        self.cache_size = 2 ** cache_size  
        self.line_size = 2 ** line_size  
        self.lines = [CacheLine(self.line_size) for _ in range(self.cache_size)]  
        self.ram = ram  

    def access(self, address):
        r = (address // self.line_size) % self.cache_size  
        t = address // (self.cache_size * self.line_size)  

        cache_line = self.lines[r]
        if cache_line.tag == t:  
            w = address % self.line_size  
            return cache_line.data[w]
        else:  
            print(f"Cache miss! Endereço {address}")  
            self.load_from_ram(address)  
            return self.access(address)  

    def load_from_ram(self, address):
        r = (address // self.line_size) % self.cache_size  
        t = address // (self.cache_size * self.line_size)  

        cache_line = self.lines[r]

        
        if cache_line.dirty:
            start_addr = (cache_line.tag * self.cache_size + r) * self.line_size
            for i in range(self.line_size):
                self.ram.write(start_addr + i, cache_line.data[i])

        start_addr = (t * self.cache_size + r) * self.line_size
        cache_line.tag = t
        for i in range(self.line_size):
            cache_line.data[i] = self.ram.read(start_addr + i)

        cache_line.dirty = False


class RAM:
    def __init__(self, address_bits):
        self.size = 2 ** address_bits  
        self.memory = [0] * self.size  

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


class EnderecoInvalido(Exception):
    def __init__(self, address):
        self.ender = address
        super().__init__(f"Endereço inválido: {address}")


try:
    ram = RAM(12)  
    cache = Cache(7, 4, ram)  

    inicio = 0
    ram.write(inicio, 110)
    ram.write(inicio + 1, 130)

    print("Valor na cache após execução:", cache.access(inicio))  
    print("Valor na cache após execução:", cache.access(inicio + 1))  

except EnderecoInvalido as e:
    print("Endereço inválido:", e.ender)  
