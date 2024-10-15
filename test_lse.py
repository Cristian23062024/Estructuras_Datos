from bed.lineales.lse import Lista_SE

if __name__ == '__main__':
    # Inicializar
    lista = Lista_SE()
    print(lista.es_vacia())
    lista.adicionar(0)
    lista.adicionar(1)
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(2)
    lista.adicionar(4)
    lista.adicionar('Udenar')
    lista.posicionar(-1, 0)
    lista.posicionar(-2, -1)
    lista.posicionar(2, 6)
    lista.posicionar(2, 14)
    lista.recorrer()
    print('')
    lista.encontrar(2)
    lista.remover(9)
    lista.remover(2, False)
    lista.recorrer()
    print('')

    for i in lista:
        print(i)
