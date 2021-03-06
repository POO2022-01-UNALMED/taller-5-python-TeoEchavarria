from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, color, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = color
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    #----M E T O D O S----
    @staticmethod
    def movimiento():
        return "saltar"

    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    #-----G E T T E R S   A N D   S E T T E R S-----
    def isVenenoso(self):
        return self._venenoso
    
    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

