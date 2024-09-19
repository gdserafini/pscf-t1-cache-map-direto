from io_class import IO
from ram import Ram
from cache import Cache
from cpu import CPU

def main() -> None:
    try:
        io = IO()
        ram = Ram(12)
        cache = Cache(7, 4, ram) 
        cpu = CPU(cache, io)

        inicio = 0
        ram.write(inicio, 110)
        ram.write(inicio+1, 130)
        cpu.run(inicio)
    except EnderecoInvalido as e:
        print("Endereco inválido:", e.ender, file=sys.stderr)

if __name__ == '__main__':
    main()
