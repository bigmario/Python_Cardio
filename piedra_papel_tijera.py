import os

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
   

def piedra_papel_tijera(input_P1, input_P2):
    # 1 = piedra
    # 2 = papel
    # 3 = tijera
    if ((input_P1 == 1 and input_P2 == 1) or 
        (input_P1 == 2 and input_P2 == 2) or 
        (input_P1 == 3 and input_P2 == 3)):
        return print('Se ha producido un empate !!!')
    elif ((input_P1 == 1 and input_P2 == 3) or 
          (input_P1 == 2 and input_P2 == 1) or 
          (input_P1 == 3 and input_P2 == 2)):
          return print('Gana el Jugador 1  !!!')
    else:
        return print('Gana el Jugador 2 !!!')



def main():
    continuar = True
    while continuar:
        print("""
        ┏━┓╻┏━╸╺┳┓┏━┓┏━┓     ┏━┓┏━┓┏━┓┏━╸╻     ┏━┓   ╺┳╸╻ ┏┓┏━╸┏━┓┏━┓
        ┣━┛┃┣╸  ┃┃┣┳┛┣━┫     ┣━┛┣━┫┣━┛┣╸ ┃     ┃ ┃    ┃ ┃  ┃┣╸ ┣┳┛┣━┫
        ╹  ╹┗━╸╺┻┛╹┗╸╹ ╹ ┛   ╹  ╹ ╹╹  ┗━╸┗━╸   ┗━┛    ╹ ╹┗━┛┗━╸╹┗╸╹ ╹    
        """)
        rounds = []
        for i in range(2):
            print(f'Jugador {i+1}, seleccione una opcion: ')
            print('[1] <- Piedra')
            print('[2] <- Papel')
            print('[3] <- Tijera\n')
            jugada=int(input())
            rounds.append(jugada)
        piedra_papel_tijera(rounds[0], rounds[1])
        pregunta = input('Otra ronda? [Y/N] ').lower()
    
        if pregunta == 'y':
            screen_clear()
        else:
            continuar = False


if __name__ == "__main__":
    main()