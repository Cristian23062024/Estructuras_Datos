from bed.lineales.cola import Cola

if __name__ == '__main__':
    cola = Cola()
    # Encolar varios elementos en la cola
    cola.encolar(5)
    cola.encolar(10)
    cola.encolar(15)
    cola.encolar(10)
    cola.encolar(12)
    cola.encolar(9)
    cola.encolar(8)
    print(f'{cola} \n')
    print(cola.frente())
    print(cola.desencolar())
    print(cola)
