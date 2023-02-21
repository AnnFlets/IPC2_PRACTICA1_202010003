class Lista:
    def __init__(self):
        self.cabeza = None
        self.contador = 0

    def estaVacia(self):
        return self.cabeza == None

    def obtenerContador(self):
        return self.contador

    def agregar(self, elemento):
        temporal = elemento
        temporal.asignarSiguiente(self.cabeza)
        self.cabeza = temporal
        self.contador += 1

    def ordenarLista(self):
        for i in range(self.contador):
            temp_apuntador_anteanterior = self.cabeza
            temp_apuntador_anterior = self.cabeza
            temp_apuntador_siguiente = temp_apuntador_anterior.obtenerSiguiente()
            contadorLista = 0
            while temp_apuntador_siguiente != None:
                if temp_apuntador_anterior.obtenerCodigo() > temp_apuntador_anterior.obtenerSiguiente().obtenerCodigo() and contadorLista == 0:
                    temp_anterior = temp_apuntador_anterior
                    temp_siguiente = temp_apuntador_siguiente
                    temp_anterior.asignarSiguiente(temp_siguiente.obtenerSiguiente())
                    temp_siguiente.asignarSiguiente(temp_anterior)
                    temp_apuntador_anterior = temp_siguiente
                    temp_apuntador_siguiente = temp_anterior
                    self.cabeza = temp_siguiente
                    self.cabeza.asignarSiguiente(temp_anterior)
                    break
                elif temp_apuntador_anterior.obtenerCodigo() > temp_apuntador_anterior.obtenerSiguiente().obtenerCodigo():
                    temp_anterior = temp_apuntador_anterior
                    temp_siguiente = temp_apuntador_siguiente
                    temp_apuntador_anteanterior.asignarSiguiente(temp_siguiente)
                    temp_anterior.asignarSiguiente(temp_siguiente.obtenerSiguiente())
                    temp_siguiente.asignarSiguiente(temp_anterior)
                    temp_apuntador_anterior = temp_siguiente
                    temp_apuntador_siguiente = temp_anterior
                if contadorLista != 0:
                    temp_apuntador_anteanterior = temp_apuntador_anteanterior.obtenerSiguiente()
                temp_apuntador_anterior = temp_apuntador_anterior.obtenerSiguiente()
                temp_apuntador_siguiente = temp_apuntador_siguiente.obtenerSiguiente()
                contadorLista += 1