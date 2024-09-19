from cache import Cache
from memory import RAM, EnderecoInvalido

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
