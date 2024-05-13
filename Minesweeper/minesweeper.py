import random
import re

# minesweeper. play the game

# create a new board object (POO) to represent the minesweeper game

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_boms = num_bombs

        # let's create the board 
        # helper function

        self.board = self.make_new_board() #board for plantting the bombs
        self.assign_values_to_board()

        # iniciar un conjunto (vacio) para llevar un seguimiento de que ubicaciones hemos descubierto 
        # cuales ubicaciones ha ido el usuario
        # we will save (row, cols) tuples into this set
        self.dug = set() #self.dug = {(0, 0)}
    
    def make_new_board(self):
        # construct a new board based on the dim size and num boom

        # generate a new board and represents an array that is the board 
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        # el array generado se ve como esto. crea una lista bidimensional donde cada elemento (board[fila][columna]) se establecen en None
        """
        board = [
            [None, None, None],  # Primera fila con 3 valores None
            [None, None, None],  # Segunda fila con 3 valores None
            [None, None, None],  # Tercera fila con 3 valores None
        ]
        """

        # plant the bombs: coloca aleatoriamente un número específico de bombas (self.num_bombs) en un tablero de juego representado por una lista bidimensional (board).
        bombs_planted = 0 # se establece en 0, para llevar la cuenta del número de bombas plantadas hasta el momento.
        while bombs_planted < self.num_boms: # mientras bombs_planted sea menor que self.num_bombs el bucle sigue colocando bombas hasta que se alcance el número deseado.
            loc = random.randint(0, self.dim_size**2 - 1) # escoge una locacion random entre el rango, que representa todas las coordenadas posibles en el tablero
            row = loc // self.dim_size # da el índice de fila donde se podría colocar la bomba.
            col = loc % self.dim_size # da el índice de columna donde se podría colocar la bomba.

            if board[row][col] == '*': 
                continue

            board[row][col] = '*' # se asigna '*' al elemento en board[row][col], indicando que se ha colocado una bomba allí.
            bombs_planted+= 1 # bombs_planted se incrementa en 1 para llevar la cuenta del total de bombas plantadas.
        
        return board # devuelve el tablero con las nuevas bombas 

    def assign_values_to_board(self):
        # we have the bombs planted, so let's assign a number 0-8 for all empty spaces 
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                self.board[r][c] == self.get_num_neighboring_bombs(r, c) #funcion da el numero de bombas que hay cerca de la fila y columna
    
    def get_num_neighboring_bombs(self, row, col): # calcula y devuelve la cantidad de bombas que rodean a una casilla específica en el tablero del juego.

        num_neighboring_bombs = 0
        # asegura que row (fila) no baje de 0 (evitando comprobaciones fuera del tablero).
        # min(self.dim_size-1, row+1) + 1 asegura que r no exceda las dimensiones del tablero e incluye la fila de arriba, de abajo y la propia fila actual (hasta +1).
        for r in range(max(0, row-1), min(self.dim_size-1, row+1) +1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1), +1):
                if r == row and c == col:
                    # our original location, dont check 
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col): # Devuelve True si la excavación es exitosa (no hay bomba) y False si se desentierra una bomba.

        # dig at that location 
        # return True if successfull dig, False if bomb dug

        self.dug.add((row, col)) 

        if self.board[row][col] == '*': #Si el elemento del tablero en esa ubicación es '*', significa que hay una bomba. devuelve False indicando una excavación fallida.
            return False
        elif self.board[row][col] > 0:
            return True
        
        # self.board[row][col] == 0: 
        # significa que no hay bomba ni número en la casilla (casilla vacía). 
        # En este caso, se procede a desenterrar las casillas vecinas de forma recursiva:

        for r in range(max(0, row-1), min(self.dim_size-1, row+1) +1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1), +1):
                if (r, c) in self.dug: #Comprueba si la casilla vecina ya ha sido desenterrada. Si lo ha sido (continue)
                    continue # dont dig where you have already dug. se salta a la siguiente iteración para evitar desenterrar la misma casilla dos veces.
                self.dig(r, c) # basicamente, permite desenterrar casillas vacías en cadena hasta encontrar una casilla con un número o una bomba.

        return True # si se llega a este punto sin encontrar una bomba, la función devuelve True indicando una excavación exitosa

    def __str__(self): 
        # magic function 
        # controla cómo se muestran como cadenas de texto los objetos de una clase. codigo legible y comprensible
        # lets create a new array that represents what the user would see

        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
              
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        #-------------------------------------------

            if isinstance(self.board[row][col], str):
                visible_board[row][col] = self.board[row][col]  # Ya es una cadena
            else:
                visible_board[row][col] = str(self.board[row][col])  # Convertir valores que no son cadenas


# play the game 
def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs 
    board = Board(dim_size, num_bombs)

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board) #ERROR 131


        #0,0 or 0, 0 or 0,  0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print('Invalid location. Try again.')
            continue

        # if it's valid, we dig 
        safe = board.dig(row, col)
        if not safe:
            # we dug in a bomb 
            break # game over

    # to end the loop:
    if safe:
        print('CONGRATULATIONS!! YOU WON!')
    else:
        print('SORRY, GAME OVER')

        # lets reveal the whole board.
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice
    play()


