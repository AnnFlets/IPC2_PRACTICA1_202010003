class Nodo:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
        self.plataforma = None
        self.siguiente = None

    def obtenerCodigo(self):
        return self.codigo

    def obtenerNombre(self):
        return self.nombre

    def obtenerPlataformas(self):
        return self.plataforma

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarSiguiente(self, siguiente):
        self.siguiente = siguiente

    def asignarPlataforma(self, plataforma):
        self.plataforma = plataforma