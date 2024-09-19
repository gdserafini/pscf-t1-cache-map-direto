from memory import MemoryInterface

class CacheLine:
    def __init__(self, size):
        self.tag = None  
        self.data = [0] * size  
        self.dirty = False  

class Cache(MemoryInterface):

    def _init_(self, cache_size, line_size, ram):
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