class TorreDeHanoi:

    def __init__(self):
        self.pilar_1 = [6, 5, 4, 3, 2, 1]
        self.pilar_2 = []
        self.pilar_3 = []

    def is_empty(self, s) :
        return len(s) == 0

    def mov_valido(self, pilar_origen, pilar_destino) :
        if self.is_empty(pilar_origen) :
            return False
        elif pilar_origen == pilar_destino :
            return False
        elif self.is_empty(pilar_destino) :
            return True
        else :
            disco = pilar_origen[-1]
            destino = pilar_destino[-1]
            if disco < destino :
                return True
            return False

    def mover_disco(self, pilar_origen, pilar_destino):
        # Recuerda que debes sacar el elemento que está más arriba en el pilar de origen
        if self.mov_valido(pilar_origen, pilar_destino) == True :
            disco = pilar_origen.pop()
        # y colocarlo en lo más alto del pilar de destino
            pilar_destino.append(disco)
        # Sacar el disco
            print()
            print('Movimiento realizado con éxito\n')
        else : 
            print()
            print('*Movimiento nulo, intenta uno nuevo*\n')

    def __str__(self):
        output = ""
        # Range termina con -1 para recorrer al revés
        for i in range(5, -1, -1):
            fila = " "  # Armamos una fila a la vez, desde arriba
            # Pilar 1
            if len(self.pilar_1) > i:
                fila += str(self.pilar_1[i]) + " "
            else:
                fila += "x "
            # Pilar 2
            if len(self.pilar_2) > i:
                fila += str(self.pilar_2[i]) + " "
            else:
                fila += "x "
            # Pilar 3
            if len(self.pilar_3) > i:
                fila += str(self.pilar_3[i]) + " "
            else:
                fila += "x "
            output += fila + "\n"
        output += "=" * 7 + "\n"
        return output
    
torre = TorreDeHanoi()
def seleccion_torre(int) :
    if int == 1 :
        return torre.pilar_1
    elif int == 2 :
        return torre.pilar_2
    elif int == 3 :
        return torre.pilar_3

while torre.is_empty(torre.pilar_1) != True \
    or torre.is_empty(torre.pilar_2) != True :
    print(torre)
    int_origen = int(input('Elige el pilar de origen (1-2-3) : '))
    int_destino = int(input('Elige el pilar de destino (1-2-3) : '))
    torre.mover_disco(seleccion_torre(int_origen),seleccion_torre(int_destino))
print('Lo lograste, eres un genio!')
print(torre)
