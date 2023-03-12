from collections import namedtuple
from random import shuffle, choice, randint  # Puedes utilizar estas funciones si lo deseas

class Juego:

    def __init__(self, turnos):

        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []

        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)

    def read_file(self):
        # Leer las cartas y guardarlas en una estructura de datos adecuada
        card_tuple = namedtuple('cards_type',['atributo','ataque','defensa'])
        with open('cards.csv') as rc :
            cards_data = []
            for line in rc :
                cards_data.append(line.strip().split(','))
            for card in cards_data :
                card[0] = card_tuple(card[0],card[1],card[2]) # Creamos la tupla nombrada
                self.mazo.append(card[0]) # Agregamos al mazo la tupla nombrada
        # NOTA: la primera fila del archivo son los atributos de las cartas

    def repartir_cartas(self):
        shuffle(self.mazo)
        self.cartas_j1 = self.mazo[0::2]
        self.cartas_j2 = self.mazo[1::2]
        self.mazo = []
        # Barajar las cartas y repartirlas de a 1

    def atacar(self, atacante, defensa):
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa
        if ptos_ataque >= ptos_defensa :
            return True
        return False

    def comenzar_juego(self, turnos):
        self.read_file()
        print('cantidad de cartas total: {}'.format(len(self.mazo)))
        self.repartir_cartas()
        for i in range(1, turnos + 1):
            j1_card = choice(self.cartas_j1)
            j2_card = choice(self.cartas_j2)
            print(f"Turno número {i}")
            print('cartas jugador {}: {}'.format(1,len(self.cartas_j1)))
            print('cartas jugador {}: {}'.format(2,len(self.cartas_j2)))
            if i % 2:
                print('Ataca el jugador uno')
                if self.atacar(j1_card, j2_card) == True :
                    print('Gana la ronda el jugador 1')
                    self.cartas_j2.remove(j2_card)
                else :
                    print('Gana la ronda el jugador 2')
                    self.cartas_j1.remove(j1_card)
                    
            else:
                print('Ataca el jugador dos')
                if self.atacar(j2_card, j1_card) == True :
                    print('Gana la ronda el jugador 2')
                    self.cartas_j1.remove(j1_card)

                else :
                    print('Gana la ronda el jugador 1')
                    self.cartas_j2.remove(j2_card)
            
            # Si alguno de los jugadores se queda sin cartas, termina la partida
            if not (len(self.cartas_j1) and len(self.cartas_j2)):
                print('Ha terminado la partida')
                if len(self.cartas_j1) < 1 :
                    print('El jugador 2 ha ganado!')
                else :
                    print('El jugador 1 ha ganado!')
                break

        print('''Se han acabado las rondas,
analizemos las estadisticas finales :''')
        final_cards_j1 = len(self.cartas_j1)
        final_cards_j2 = len(self.cartas_j2)
        print('cartas jugador {}: {} | cartas jugador {}: {}'.\
              format(1,final_cards_j1,2,final_cards_j2))
        if final_cards_j1 > final_cards_j2 :
            print('El jugador 1 ha ganado!')
        elif final_cards_j1 < final_cards_j2 :
            print('El jugador 2 ha ganado!')
        else :
            print('Tenemos un empate damas y caballeros!')

print('Let\'s play Pro-gra-oh!')
print('This is a random game, you don\'t need do anything')
rounds = int(input('How many rounds would you like has this game? :'))
juego = Juego(rounds)