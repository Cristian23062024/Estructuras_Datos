from bed.lineales.lde import Lista_DE

if __name__ == '__main__':
    lista = Lista_DE()
    
    print(lista.es_vacia())
    
    print(lista.adicionar(1))
    lista.adicionar(2)
    lista.adicionar(3)
    lista.adicionar(4)
    lista.adicionar(5)
    lista.adicionar(6)
    lista.adicionar(7)
    lista.adicionar(8)
    lista.adicionar(6)
    lista.adicionar(10)
    lista.adicionar(11)
    lista.adicionar(6)
    lista.adicionar(13)
    lista.adicionar(14)
    lista.adicionar(15)
    print(lista.adicionar('Udenar'))
    
    print(lista.posicionar(100, 5))
    print(lista.posicionar(200, 15))
    print(lista.posicionar(300, 25))
    
    print(lista.encontrar(100))
    
    print(lista.ubicar(6))
    
    print('')
    
    print(lista.adelante())
    
    print(lista.__len__())
    
    print(lista.remover(2))
    
    print(lista.remover(6, False))
    
    print(lista)
    
    
    