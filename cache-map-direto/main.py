from cache import Cache
from memory import RAM, EnderecoInvalido

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
